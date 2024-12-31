#jobSearch/models.py

from django.db import models

class JobSearch(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    experience = models.IntegerField()
    location = models.CharField(max_length=255)
    work_mode = models.CharField(max_length=50, choices=[
        ('Work From Home', 'Work From Home'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote')
    ])
    expertise = models.JSONField()
    salary = models.FloatField()
    department = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)

    def __str__(self):
        return self.title
