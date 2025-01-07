# empregistration/serializers.py


from rest_framework import serializers
from django.contrib.auth.models import User
from empregistration.models import empUserProfile

class empUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = empUserProfile
        fields = ['full_name', 'mobile_number', 'company_name']

class empRegisterSerializer(serializers.ModelSerializer):
    emp_profile = empUserProfileSerializer()

    class Meta:
        model = User
        fields = ['email', 'password', 'emp_profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('emp_profile')
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            password=validated_data['password']
        )
        empUserProfile.objects.create(
            user=user,
            full_name=profile_data['full_name'],
            mobile_number=profile_data['mobile_number'],
            company_name=profile_data['company_name'],
        )
        return user
