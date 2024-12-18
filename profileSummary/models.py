from django.db import models
from django.contrib.auth.models import User

class ProfileSummary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summary = models.TextField()

    def _str_(self):
        return f"{self.user.username}'s Profile Summary"