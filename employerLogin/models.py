#employerLogin/models.py

from django.conf import settings
from django.db import models

class employerLogin(models.Model):
    # Reference the user dynamically
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the CustomUser model from homeRegistration
        on_delete=models.CASCADE,
        related_name='employer_login',  # Optional: to enable reverse lookup
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"employerLogin for {self.user.username} at {self.login_time}"
    
