import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import EmailSerializer, OTPVerificationSerializer, ResetPasswordSerializer

# Simulate OTP generation (In real scenarios, you can use external libraries like django-otp)
OTP_STORE = {}

@api_view(['POST'])
def send_otp(request):
    # Validate the email
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        # Check if the email exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Email not registered'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate and send OTP
        otp = str(random.randint(100000, 999999))
        OTP_STORE[email] = otp
        
        send_mail(
            'Your OTP for password reset',
            f'Your OTP is: {otp}',
            'no-reply@jobgenee.com',
            [email],
            fail_silently=False,
        )
        
        return Response({'message': 'OTP sent successfully!'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_otp(request):
    # Validate the OTP
    serializer = OTPVerificationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        # Check if OTP matches
        if OTP_STORE.get(email) == otp:
            return Response({'message': 'OTP verified successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_password(request):
    # Validate the email and new password
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        new_password = serializer.validated_data['new_password']

        # Check if the email exists in the database
        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successfully!'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Email not registered'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
