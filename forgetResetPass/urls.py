#ForgotPass/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('forResetPass', views.ForgotAndResetPasswordView.as_view(), name='forResetPass'),
]
