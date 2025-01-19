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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    date_issued = models.DateField()

class Education(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50)

class Project(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()