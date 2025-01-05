# empregistration/serializers.py


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import OTP
import re

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    mobile_number = serializers.CharField(write_only=True)
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'mobile_number', 'company_name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate_mobile_number(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Enter a valid 10-digit mobile number.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )
        user.set_password(password)
        user.save()
        return user

class OTPSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = OTP
        fields = ['email']

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is not registered.")
        return value
