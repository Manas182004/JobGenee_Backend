from django.urls import path
from .views import EmployerRegistrationView, EmployerPortalView

urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer-register'),
    path('portal/', EmployerPortalView.as_view(), name='employer-portal'),
]