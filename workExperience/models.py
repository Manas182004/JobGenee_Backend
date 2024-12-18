from django.db import models
from django.contrib.auth.models import User

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_experiences")
    is_current_job = models.BooleanField(default=False)
    employment_type = models.CharField(max_length=50, choices=[("Full time", "Full time"), ("Internship", "Internship")], blank=True)
    total_experience_months = models.PositiveIntegerField(null=True, blank=True)
    total_experience_years = models.PositiveIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    current_salary = models.FloatField(null=True, blank=True)
    salary_currency = models.CharField(max_length=10, choices=[("INR", "Rupees (INR)"), ("USD", "USD")], blank=True)
    utilized_skills = models.TextField(blank=True)
    notice_period = models.CharField(max_length=50, choices=[
        ("15 days or less", "15 days or less"),
        ("1 month", "1 month"),
        ("2 months", "2 months"),
        ("3 months", "3 months"),
        ("more than 3 months", "more than 3 months"),
    ], blank=True)

    def _str_(self):
        return f"{self.user.username} - {self.company_name}"