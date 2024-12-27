#homeRegistration/models.py

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class UserProfile(models.Model):
    WORK_STATUS_CHOICES = [
        ('fresher', "I'm a Fresher"),
        ('experienced', "I'm Experienced"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = PhoneNumberField(null=False, blank=False, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_verified = models.BooleanField(default=False)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES)
    current_city = models.CharField(max_length=100, null=True, blank=True)
    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

