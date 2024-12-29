from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='job_postings')
    locations = models.ManyToManyField(Location, related_name='job_postings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
