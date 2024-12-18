from django.urls import path
from .views import WorkExperienceListCreateView, WorkExperienceRetrieveUpdateDeleteView

urlpatterns = [
    path('work-experiences/', WorkExperienceListCreateView.as_view(), name='work-experience-list-create'),
    path('work-experiences/<int:pk>/', WorkExperienceRetrieveUpdateDeleteView.as_view(), name='work-experience-detail'),
]