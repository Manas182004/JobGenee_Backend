from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, LocationViewSet, JobPostingViewSet

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('locations', LocationViewSet)
router.register('job-postings', JobPostingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
