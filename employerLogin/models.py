# #employerLogin/models.py

# from django.contrib.auth.models import User
# from django.db import models

# class empUserProfile(models.Model):
#     ROLE_CHOICES = [
#         ('employer', 'Employer'),
#         ('employee', 'Employee'),  # Add other roles here if needed
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='login_profile')
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"

# # Signal to create a UserProfile automatically when a User is created
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         empUserProfile.objects.create(user=instance)
