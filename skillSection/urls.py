from django.urls import path
from .views import SkillListCreateView, SkillUpdateDeleteView

urlpatterns = [
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillUpdateDeleteView.as_view(), name='skill-update-delete'),
]
