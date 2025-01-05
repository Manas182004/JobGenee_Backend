#empregistration/view.py


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import OTP
from .serializers import RegisterSerializer, OTPSerializer
import random

class SendOtpView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user, created = User.objects.get_or_create(email=email)

            otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
            OTP.objects.update_or_create(user=user, defaults={'otp': otp})

            # Send OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is: {otp}',
                'manasharma767@gmail.com',  # Use your configured email
                [email],
                fail_silently=False,
            )
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        otp = request.data.get('otp')
        email = request.data.get('email')

        # Validate OTP
        try:
            user = User.objects.get(email=email)
            user_otp = OTP.objects.get(user=user)
            if not user_otp.is_valid():
                return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            if user_otp.otp != otp:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, OTP.DoesNotExist):
            return Response({'error': 'Invalid email or OTP'}, status=status.HTTP_400_BAD_REQUEST)

        # Register the user
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_otp.delete()  # Remove OTP after successful registration
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
