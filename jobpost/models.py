#jobpost/models.py

from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=80)
    job_description = models.TextField()
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, default="INR")
    work_type = models.CharField(max_length=20, choices=[('In-Office', 'In-Office'), ('Hybrid', 'Hybrid'), ('Remote', 'Remote')], default='In-Office')
    employment_type = models.CharField(max_length=20, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract'), ('Internship', 'Internship')], default='Full Time')
    location = models.JSONField(default=list)  # Store multiple locations as a JSON list
    skills = models.JSONField(default=list)  # Store skills as a JSON list
    education_level = models.CharField(max_length=50, null=True, blank=True)
    uploaded_file = models.FileField(upload_to='job_descriptions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title
