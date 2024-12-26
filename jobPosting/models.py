from django.db import models
from django.conf import settings

class JobPosting(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="jobPosting"
    )
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    work_type = models.CharField(max_length=50, choices=[
        ('In-Office', 'In-Office'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),
    ])
    location = models.JSONField()  # Store multiple locations as JSON
    skills = models.JSONField()  # Store skills as JSON
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_currency = models.CharField(max_length=10, default='INR')
    employment_type = models.CharField(max_length=50, choices=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ])
    education_level = models.CharField(max_length=50, null=True, blank=True)
    jd_file = models.FileField(upload_to='job_descriptions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title
