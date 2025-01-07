# empregistration/urls.py


from django.urls import path
from .views import empRegisterView, VerifyOTPview
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', empRegisterView.as_view(), name='register'),
    path('verify-otp/', VerifyOTPview.as_view(), name='verify-otp'),
    path('obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]