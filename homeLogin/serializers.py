from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.timezone import now
from .models import homeLogin

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Use email instead of username since your project uses email as the username
        user = authenticate(username=data.get("email"), password=data.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        # Check if user is active
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive")

        # Log user login in homeLogin model
        homeLogin.objects.create(user=user, login_time=now())

        return {"user": user}
