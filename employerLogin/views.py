import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from empregistration.models import empUserProfile  # Import your profile model
from rest_framework_simplejwt.tokens import RefreshToken

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

        # Cache the OTP with a timeout of 5 minutes
        cache.set(f'otp_{email}', otp, timeout=300)

        # Send OTP via email
        send_mail(
            subject="Your OTP for Login",
            message=f"Your OTP is {otp}. It is valid for 5 minutes.",
            from_email="manasharma767@gmail.com",
            recipient_list=[email],
        )
        
        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

class VerifyOtpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response({"error": "Email and OTP are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve OTP from cache
        cached_otp = cache.get(f'otp_{email}')

        if not cached_otp:
            return Response({"error": "OTP expired or invalid"}, status=status.HTTP_400_BAD_REQUEST)

        if str(cached_otp) != str(otp):
            return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check the user's role from the EmpUserProfile table
        try:
            emp_profile = empUserProfile.objects.get(user=user)
        except empUserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        if emp_profile.role != "employer":
            return Response({"error": "Access restricted to employers only"}, status=status.HTTP_403_FORBIDDEN)

        # Delete OTP from cache after successful verification
        cache.delete(f'otp_{email}')

        return Response({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "role": emp_profile.role,
            }
        }, status=status.HTTP_200_OK)