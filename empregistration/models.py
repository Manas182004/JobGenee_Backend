from django.db import models

class Employer(models.Model):
    
    empRemail = models.EmailField(unique=True)
    empRmobile = models.CharField(max_length=15)
    empRpassword = models.CharField(max_length=128)  # Store hashed password for security

    def __str__(self):
        return self.empRemail
