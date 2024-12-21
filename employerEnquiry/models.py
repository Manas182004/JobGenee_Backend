# api/models.py
from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    company_type = models.CharField(max_length=100)
    employees = models.IntegerField()
    role = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
