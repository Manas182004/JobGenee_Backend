#employerLogin/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        # Authenticate the user
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        data['user'] = user
        return data
