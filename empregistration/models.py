# empregistration/models.py


from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class empUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp_profile')
    company_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.first_name} - {self.company_name}"

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        expiration_time = timedelta(minutes=10)
        return now() - self.created_at <= expiration_time

    def __str__(self):
        return f"OTP for {self.user.email}: {self.otp}"
