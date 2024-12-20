from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from .models import homeLogin
from django.utils import timezone

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Parse the incoming data using the serializer
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Instead of using serializer validation for user, we now authenticate using email
        user = authenticate(request, username=serializer.validated_data["username"], password=serializer.validated_data["password"])

        # Check if authentication was successful
        if not user:
            return Response({"error": "Invalid username or password"}, status=400)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Log the login activity
        login_instance = homeLogin.objects.create(
            user=user,
            login_time=timezone.now()
        )

        # Respond with the generated tokens and login details
        return Response({
            "refresh": str(refresh),
            "access": access_token,
            "username": user.username,  # Assuming username is in the CustomUser model
            "email": user.email,
            "login_time": login_instance.login_time,
        })
