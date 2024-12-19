from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    company_type = models.CharField(max_length=50, choices=[('Company', 'Company'), ('Consultant', 'Consultant')])
    employee_count = models.PositiveIntegerField()
    role = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('homeRegistration.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name