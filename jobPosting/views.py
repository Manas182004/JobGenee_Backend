from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination
from .models import JobPosting
from .serializers import JobPostingSerializer

# Custom pagination class
class JobPostingPagination(PageNumberPagination):
    page_size = 10  # Customize page size
    page_size_query_param = 'page_size'
    max_page_size = 100

class JobPostingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing job postings.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    pagination_class = JobPostingPagination

    def perform_create(self, serializer):
        # Associate the job posting with the authenticated user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Employers see their job postings; job seekers see all job postings
        if self.request.user.is_staff or hasattr(self.request.user, 'is_employer') and self.request.user.is_employer:
            return self.queryset.filter(user=self.request.user).select_related('user')
        return self.queryset
