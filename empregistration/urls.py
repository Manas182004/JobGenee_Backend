# empregistration urls.py
from django.urls import path
from .views import SendOtpView, RegisterView

urlpatterns = [
    path('empsend-otp/', SendOtpView.as_view(), name='send_otp'),
    path('empregister/', RegisterView.as_view(), name='register'),
]
