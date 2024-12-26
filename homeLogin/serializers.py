from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    homeEmail = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        homeEmail = data.get('homeEmail')
        password = data.get('password')

        if not homeEmail or not password:
            raise serializers.ValidationError(
                {"detail": "Both email and password are required.", "code": "missing_credentials"}
            )

        # Authenticate the user
        user = authenticate(username=homeEmail, password=password)
        if user is None:
            raise serializers.ValidationError(
                {"detail": "Invalid credentials.", "code": "invalid_credentials"}
            )
        if not user.is_active:
            raise serializers.ValidationError(
                {"detail": "This account is inactive. Contact support.", "code": "inactive_account"}
            )

        data['user'] = user
        return data
