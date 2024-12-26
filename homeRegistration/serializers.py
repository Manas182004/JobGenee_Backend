#homeRegistration/serializers.py

from rest_framework import serializers
from .models import HomeRegistration


class HomeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeRegistration
        fields = [
            "id",
            "user",
            "homeCurrent_city",
            "homeResume",
            "homeWork_status",
            "otp",
            "is_verified",
        ]
        read_only_fields = ["user", "is_verified", "otp"]
