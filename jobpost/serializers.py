from rest_framework import serializers
from .models import Skill, Location, JobPosting

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class JobPostingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    skills = SkillSerializer(many=True)
    locations = LocationSerializer(many=True)

    class Meta:
        model = JobPosting
        fields = ['id', 'user', 'title', 'description', 'skills', 'locations', 'created_at']

    def create(self, validated_data):
        skills_data = validated_data.pop('skills')
        locations_data = validated_data.pop('locations')
        job = JobPosting.objects.create(**validated_data)
        for skill in skills_data:
            skill_obj, created = Skill.objects.get_or_create(name=skill['name'])
            job.skills.add(skill_obj)
        for location in locations_data:
            location_obj, created = Location.objects.get_or_create(name=location['name'])
            job.locations.add(location_obj)
        return job
