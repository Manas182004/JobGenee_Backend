# dashboard/views.py


from .models import BasicInformation, Certification, Education, Experience, Language, Project
from .serializers import (BasicInformationSerializer, CertificationSerializer,
                          EducationSerializer, ExperienceSerializer,
                          LanguageSerializer, ProjectSerializer)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer

    def list(self, request, *args, **kwargs):
        # Fetch only the first record
        info = BasicInformation.objects.first()
        if info:
            serializer = self.get_serializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Basic information not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        # Update the first record
        info = BasicInformation.objects.first()
        if info:
            serializer = self.get_serializer(info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Basic information not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload_resume(self, request, *args, **kwargs):
        # Handle resume file upload
        info = BasicInformation.objects.first()
        if not info:
            info = BasicInformation.objects.create()
        info.resume_file = request.FILES['resume_file']
        info.save()
        return Response({"detail": "File uploaded successfully"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def download_resume(self, request, *args, **kwargs):
        # Handle resume file download
        info = BasicInformation.objects.first()
        if info and info.resume_file:
            file_url = info.resume_file.url
            return Response({"file_url": file_url}, status=status.HTTP_200_OK)
        return Response({"detail": "No file uploaded"}, status=status.HTTP_404_NOT_FOUND)

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer