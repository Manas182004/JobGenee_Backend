from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeRegistration(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="homeRegistration"
    )
    homeCurrent_city = models.CharField(max_length=100)
    homeResume = models.FileField(upload_to="resumes/")
    homeWork_status = models.CharField(
        max_length=20, choices=[("fresher", "Fresher"), ("experienced", "Experienced")]
    )
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Registration for {self.user.homeFull_name}"
