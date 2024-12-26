from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HomeRegistration
from .serializers import HomeRegistrationSerializer
from .utils import generate_otp, send_otp_email


class HomeRegistrationView(APIView):
    """
    Handles registration.
    """
    def post(self, request, *args, **kwargs):
        serializer = HomeRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Generate OTP and associate it with the registration
            otp = generate_otp()
            serializer.save(user=request.user, otp=otp)
            # Send OTP via email
            send_otp_email(request.user.homeEmail, otp)
            return Response({"message": "Registration successful. OTP sent."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpView(APIView):
    """
    Verifies the OTP for a home registration.
    """
    def post(self, request, *args, **kwargs):
        otp = request.data.get("otp")
        try:
            registration = HomeRegistration.objects.get(user=request.user, otp=otp)
            registration.is_verified = True
            registration.otp = None  # Clear OTP after verification
            registration.save()
            return Response({"message": "Registration verified successfully."}, status=status.HTTP_200_OK)
        except HomeRegistration.DoesNotExist:
            return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
