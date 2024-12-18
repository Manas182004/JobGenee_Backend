from django.urls import path
from .views import ResumeUploadView, ResumeDownloadView

urlpatterns = [
    path('resume/upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('resume/download/', ResumeDownloadView.as_view(), name='resume-download'),
]