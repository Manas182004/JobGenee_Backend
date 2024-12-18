from django.urls import path
from .views import CoverLetterUploadView, CoverLetterDownloadView

urlpatterns = [
    path('cover-letter/upload/', CoverLetterUploadView.as_view(), name='cover-letter-upload'),
    path('cover-letter/download/', CoverLetterDownloadView.as_view(), name='cover-letter-download'),
]