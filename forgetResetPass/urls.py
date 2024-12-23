from django.urls import path
from . import views

urlpatterns = [
    path('forgetsend-otp/', views.send_otp, name='send_otp'),
    path('forgetverify-otp/', views.verify_otp, name='verify_otp'),
    path('forgetreset-password/', views.reset_password, name='reset_password'),
]
