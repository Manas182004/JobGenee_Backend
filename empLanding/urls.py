#empLanding/urls.py

from django.urls import path
from .views import get_jobs

urlpatterns = [
    path('jobs/', get_jobs, name='get_jobs'),
    # path('jobs/<int:id>/apply/', JobApplyView.as_view(), name='job-apply'),
]

