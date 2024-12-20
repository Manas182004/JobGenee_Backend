#homeLogin/models.py

from django.conf import settings
from django.db import models
from datetime import timedelta

class homeLogin(models.Model):
    # Reference the user dynamically
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the CustomUser model
        on_delete=models.CASCADE,
        related_name='home_login',  # Optional: to enable reverse lookup
    )
    login_time = models.DateTimeField(auto_now_add=True, db_index=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def session_duration(self):
        if self.logout_time:
            return self.logout_time - self.login_time
        return timedelta(days=1)  # Active session

    def __str__(self):
        return f"homeLogin for {self.user.email} at {self.login_time}"
