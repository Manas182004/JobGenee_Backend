#empregistration/models.py

from django.contrib.auth.models import User
from django.db import models

class empUserProfile(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('employee', 'Employee'),  # You can add more roles if needed
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp_profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

# Signal to automatically create a profile when a user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        empUserProfile.objects.create(user=instance)