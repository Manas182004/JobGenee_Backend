#ForgotPass/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import re

class ForgotAndResetPasswordView(APIView):
    def post(self, request):
        """
        Handle sending password reset link or validating token for resetting the password.
        If 'email' is provided: Send reset link.
        If 'uidb64', 'token', and 'new_password' are provided: Reset password.
        """
        email = request.data.get('email', '').strip()
        uidb64 = request.data.get('uidb64')
        token = request.data.get('token')
        new_password = request.data.get('new_password', '').strip()

        # Case 1: Sending the reset password link
        if email:
            if not email:
                return Response({"error": "Email field is empty."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email=email)
                # Generate token and UID
                token = default_token_generator.make_token(user)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                # Send reset password email
                reset_link = f'https://example.com/reset-password?uidb64={uidb64}&token={token}'
                send_mail(
                    'Password Reset Request',
                    f'Use this link to reset your password: {reset_link}',
                    'noreply@example.com',
                    [email],
                    fail_silently=False,
                )

                return Response(
                    {"message": "Password reset link sent to your email."},
                    status=status.HTTP_200_OK
                )
            except User.DoesNotExist:
                return Response(
                    {"error": "We cannot find your email."},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Case 2: Resetting the password
        elif uidb64 and token and new_password:
            # Validate password strength
            password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
            if not re.match(password_regex, new_password):
                return Response(
                    {"error": "Password must be at least 8 characters long, contain a lowercase letter, an uppercase letter, a number, and a special character."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            try:
                # Decode user ID
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)

                # Check token validity
                if not default_token_generator.check_token(user, token):
                    return Response(
                        {"error": "Invalid or expired token."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Update password
                user.password = make_password(new_password)
                user.save()

                return Response(
                    {"message": "Password has been reset successfully."},
                    status=status.HTTP_200_OK
                )
            except (User.DoesNotExist, ValueError, TypeError):
                return Response(
                    {"error": "Invalid user."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Missing required fields for both cases
        return Response(
            {"error": "Invalid request. Please provide either 'email' or 'uidb64', 'token', and 'new_password'."},
            status=status.HTTP_400_BAD_REQUEST
        )