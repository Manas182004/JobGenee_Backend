from django.urls import path
from .views import submit_enquiry

urlpatterns = [
    path('enquiry/', submit_enquiry, name='submit-enquiry'),
]
