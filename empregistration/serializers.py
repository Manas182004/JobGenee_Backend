#empregistration/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import empUserProfile  # Import empUserProfile model

class EmployerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Hide password in responses
        }

    def create(self, validated_data):
        # Set the username as the email
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        # Assign the "employer" role
        user.emp_profile.role = 'employer'
        user.emp_profile.save()
        return user
