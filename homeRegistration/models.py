from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    current_city = models.CharField(max_length=255, blank=True)