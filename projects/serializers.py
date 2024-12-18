from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_status', 'worked_from_year', 'worked_from_month', 'completed_on_month', 'completed_on_date', 'project_details']
