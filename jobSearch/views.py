#jobSearch/views.py


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.cache import cache
from .models import JobSearch
from .serializers import JobSerializer

class JobPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class JobListCreateAPIView(ListCreateAPIView):
    queryset = JobSearch.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = JobPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['work_mode', 'experience', 'department', 'qualification']
    search_fields = ['title', 'company', 'location', 'expertise']

    def get_queryset(self):
        cached_jobs = cache.get('jobs')
        if cached_jobs:
            return cached_jobs
        queryset = super().get_queryset()
        cache.set('jobs', queryset, timeout=60 * 15)  # Cache for 15 minutes
        return queryset

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        response.data = {
            "error": True,
            "message": str(exc)
        }
        return response

class JobDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = JobSearch.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        response.data = {
            "error": True,
            "message": str(exc)
        }
        return response
