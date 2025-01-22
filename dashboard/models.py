# dashboard/models.py


from django.db import models
from django.contrib.auth.models import User

class BasicInformation(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    other_links = models.TextField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    experience = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    ctc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)

class Certification(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField()

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Experience(models.Model):
    job_title = models.CharField(max_length=255, blank=True, null=True)
    job_role = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField()

class Language(models.Model):
    LANGUAGE_PROFICIENCY_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Proficient", "Proficient"),
        ("Fluent", "Fluent"),
    ]
    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20, choices=LANGUAGE_PROFICIENCY_CHOICES)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    timeline = models.PositiveIntegerField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)