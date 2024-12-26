from django.urls import path
from .views import EmployerRegistrationView

urlpatterns = [
    path('employer/register/', EmployerRegistrationView.as_view(), name='employer-register'),
]
