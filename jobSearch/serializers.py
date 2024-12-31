#jobSearch/serializers.py

from rest_framework import serializers
from .models import JobSearch

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSearch
        fields = '__all__'

    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Salary must be a positive number.")
        return value

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience must be a non-negative number.")
        return value

