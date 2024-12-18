from django.urls import path
from .views import ProfileSummaryView

urlpatterns = [
    path('profile-summary/', ProfileSummaryView.as_view(), name='profile-summary'),
]