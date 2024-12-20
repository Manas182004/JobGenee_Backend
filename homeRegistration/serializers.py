#homeRegistration/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.validators import RegexValidator

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['mobile_number', 'work_status', 'current_city', 'resume', 'otp', 'otp_verified']

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'confirm_password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        # Validate Password
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # Validate Email Format
        if not data['email']:
            raise serializers.ValidationError({"email": "Email is required."})
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        UserProfile.objects.create(
            user=user,
            mobile_number=profile_data['mobile_number'],
            work_status=profile_data['work_status'],
            current_city=profile_data.get('current_city', None),
            resume=profile_data.get('resume', None),
        )
        return user
