#customUser/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, homeEmail, password=None, **extra_fields):
        if not homeEmail:
            raise ValueError("The homeEmail field must be set")
        homeEmail = self.normalize_email(homeEmail)
        user = self.model(homeEmail=homeEmail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, homeEmail, password=None, **extra_fields):
        extra_fields.setdefault("homeIs_staff", True)
        extra_fields.setdefault("homeIs_superuser", True)
        return self.create_user(homeEmail, password, **extra_fields)

class CustomUser(AbstractUser):
    # Role-Based Fields
    
#jobPosting API__________________________________
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')

    # Employer-Specific Fields
    is_employer = models.BooleanField(default=False)
    is_approved_employer = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    # Contact Information
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Job Posting Metadata
    total_jobs_posted = models.PositiveIntegerField(default=0)  # For tracking jobs posted by the user

    # Job Seeker-Specific Fields
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)  # JSON array of skills
    preferred_location = models.JSONField(blank=True, null=True)  # JSON array of preferred locations
    
   #empregistration API_________________________________
   
    empRemail = models.EmailField(unique=True)  # Replacing email with empRemail
    empRmobile = models.CharField(max_length=15, blank=True, null=True)  # Replacing mobile
    empRpassword = models.CharField(max_length=128)  # For storing hashed password

    USERNAME_FIELD = 'empRemail'
    REQUIRED_FIELDS = ['empRmobile']

    def __str__(self):
        return self.empRemail
    
#homeRegistration API____________________________________________
    
    homeEmail = models.EmailField(unique=True)
    homeFull_name = models.CharField(max_length=255)
    homeMobile_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r"^\+?\d{10,15}$", "Enter a valid mobile number.")],
    )
    homeCurrent_city = models.CharField(max_length=100, null=True, blank=True)
    homeResume = models.FileField(upload_to="resumes/", null=True, blank=True)
    homeWork_status = models.CharField(
        max_length=20, choices=[("fresher", "Fresher"), ("experienced", "Experienced")]
    )

    homeIs_active = models.BooleanField(default=True)
    homeIs_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "homeEmail"
    REQUIRED_FIELDS = ["homeFull_name", "homeMobile_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.homeEmail
    






