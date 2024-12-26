from django.urls import path
from .views import HomeRegistrationView, VerifyOtpView

urlpatterns = [
    path("register/", HomeRegistrationView.as_view(), name="register"),
    path("verify-otp/", VerifyOtpView.as_view(), name="verify-otp"),
]
