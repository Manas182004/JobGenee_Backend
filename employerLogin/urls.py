from django.urls import path
from .views import SendOtpView, VerifyOtpView

urlpatterns = [
    path('send-otp1/', SendOtpView.as_view(), name='send-otp'),
    path('verify-otp2/', VerifyOtpView.as_view(), name='verify-otp'),
]