from rest_framework import serializers
from customUser.models import CustomUser

class EmployerRegistrationSerializer(serializers.ModelSerializer):
    empRpassword = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['empRemail', 'empRmobile', 'empRpassword']

    def create(self, validated_data):
        # Use `create_user` to hash the password
        user = CustomUser.objects.create_user(
            empRemail=validated_data['empRemail'],
            empRmobile=validated_data['empRmobile'],
            password=validated_data['empRpassword']  # Django hashes it internally
        )
        return user
