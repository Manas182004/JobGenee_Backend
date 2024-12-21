from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from .models import UserProfile
from .utils import generate_otp, send_otp_email


class RegisterView(APIView):
    """
    Handles user registration and sends an OTP for verification.
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Save user and profile
            user = serializer.save()
            profile = user.profile

            # Generate and send OTP
            otp = generate_otp()
            profile.otp = otp
            profile.save()

            try:
                send_otp_email(user.email, otp)
            except Exception as e:
                # Handle email sending failure
                return Response(
                    {"error": "Failed to send OTP. Please try again later.", "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Registration successful. OTP sent to your email.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    """
    Verifies the OTP sent to the user's email.
    """
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        # Validate input
        if not email or not otp:
            return Response(
                {"error": "Email and OTP are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Retrieve the profile by email
            profile = UserProfile.objects.get(user__email=email)

            # Check if already verified
            if profile.otp_verified:
                return Response({"message": "Account is already verified."}, status=status.HTTP_200_OK)

            # Validate OTP
            if profile.otp == otp:
                profile.otp_verified = True
                profile.save()
                return Response({"message": "OTP verified successfully."}, status=status.HTTP_200_OK)

            return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

        except UserProfile.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
