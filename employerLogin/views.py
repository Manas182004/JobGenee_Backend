#employerLogin/views.py

import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SendOtpView(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Generate a random 6-digit OTP
        otp = random.randint(100000, 999999)

        # Cache the OTP with a timeout of 5 minutes (300 seconds)
        cache.set(f'otp_{email}', otp, timeout=300)

        # Send OTP via email
        try:
            send_mail(
                subject="Your OTP for Login",
                message=f"Your OTP is {otp}. It is valid for 5 minutes.",
                from_email="manasharma767@gmail.com",
                recipient_list=[email],
            )
        except Exception as e:
            return Response({"error": f"Failed to send OTP: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)


class VerifyOtpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        password = request.data.get('password')

        if not email or not otp or not password:
            return Response({"error": "Email, OTP, and Password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve OTP from cache
        cached_otp = cache.get(f'otp_{email}')
        if not cached_otp:
            return Response({"error": "OTP expired or invalid."}, status=status.HTTP_400_BAD_REQUEST)

        if str(cached_otp) != str(otp):
            return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=email, password=password)
        if not user:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({"error": "This account is inactive."}, status=status.HTTP_403_FORBIDDEN)

        # Delete OTP from cache after successful verification
        cache.delete(f'otp_{email}')

        return Response({
            "message": "Login successful!",
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            }
        }, status=status.HTTP_200_OK)