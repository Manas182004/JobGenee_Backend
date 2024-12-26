from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeRegistrationViewSet, VerifyOtpView

router = DefaultRouter()
router.register(r"home-registration", HomeRegistrationViewSet, basename="home-registration")

urlpatterns = [
    path("", include(router.urls)),
    path("verify-otp/", VerifyOtpView.as_view(), name="verify-otp"),
]
