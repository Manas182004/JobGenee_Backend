from rest_framework import serializers
from .models import ProfileSummary

class ProfileSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSummary
        fields = ['id', 'summary']