from rest_framework import serializers
from .models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        # Ensure salary range is valid
        if data.get('salary_from') and data.get('salary_to'):
            if data['salary_from'] > data['salary_to']:
                raise serializers.ValidationError("Salary 'from' must be less than 'to'.")
        # Ensure at least one skill is selected
        if not data.get('skills'):
            raise serializers.ValidationError("At least one skill is required.")
        return data
