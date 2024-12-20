#employerEnquiry/models.py

from django.db import models
from django.conf import settings


class employerEnquiry(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the CustomUser model from homeRegistration
        on_delete=models.CASCADE,
        related_name='employer_enquiry',
     )
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    company_type = models.CharField(max_length=50, choices=[('Company', 'Company'), ('Consultant', 'Consultant')])
    employee_count = models.PositiveIntegerField()
    role = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name