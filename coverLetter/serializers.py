from rest_framework import serializers
from .models import CoverLetter

class CoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverLetter
        fields = ['id', 'file', 'uploaded_at']