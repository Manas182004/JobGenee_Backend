#ForgotPass/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForgotAndResetPasswordView.as_view(), name='forgot-reset-password'),
]
