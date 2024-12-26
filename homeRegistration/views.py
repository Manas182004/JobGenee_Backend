from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HomeRegistration
from .serializers import HomeRegistrationSerializer
import random

class HomeRegistrationViewSet(viewsets.ModelViewSet):
    """
    Handles registration CRUD operations.
    """
    queryset = HomeRegistration.objects.all()
    serializer_class = HomeRegistrationSerializer

    def perform_create(self, serializer):
        # Associate the logged-in user and generate OTP
        otp = f"{random.randint(100000, 999999)}"  # Generate a 6-digit OTP
        serializer.save(user=self.request.user, otp=otp)
        # Send OTP (Placeholder)
        print(f"OTP for {self.request.user.homeEmail}: {otp}")


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
            return Response({"message": "Registration verified successfully."})
        except HomeRegistration.DoesNotExist:
            return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
