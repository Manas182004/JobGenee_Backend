# empregistration/models.py


from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.utils.timezone import now, timedelta
from django.utils import timezone


class empUserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp_profile')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    mobile_number = PhoneNumberField(null=False, blank=False, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

