from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    project_title = models.CharField(max_length=255)
    project_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    worked_from_year = models.CharField(max_length=4, null=True, blank=True)
    worked_from_month = models.CharField(max_length=2, null=True, blank=True)
    completed_on_month = models.CharField(max_length=2, null=True, blank=True)
    completed_on_date = models.DateField(null=True, blank=True)
    project_details = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def _str_(self):
        return self.project_title
