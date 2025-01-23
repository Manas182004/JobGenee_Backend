#jobpost/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

# Set up the DRF router
router = DefaultRouter()
router.register(r'jobs', JobViewSet)

# Define the app's urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]
