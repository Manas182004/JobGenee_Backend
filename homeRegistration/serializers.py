from rest_framework import serializers
from django.contrib.auth.models import User
from homeRegistration.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'mobile_number', 'work_status', 'current_city', 'resume']

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            password=validated_data['password']
        )
        UserProfile.objects.create(
            user=user,
            full_name=profile_data['full_name'],
            mobile_number=profile_data['mobile_number'],
            work_status=profile_data['work_status'],
            current_city=profile_data.get('current_city', None),
            resume=profile_data.get('resume', None),
        )
        return user
