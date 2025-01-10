# dashboard/views.py


from .models import BasicInformation, Certification, Education, Experience, Language, Project
from .serializers import (BasicInformationSerializer, CertificationSerializer,
                          EducationSerializer, ExperienceSerializer,
                          LanguageSerializer, ProjectSerializer)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.models import User
    
class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer

    def list(self, request, *args, **kwargs):
        info = BasicInformation.objects.first()
        if info:
            serializer = self.get_serializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Basic information not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
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
        info = BasicInformation.objects.first() or BasicInformation.objects.create()
        if 'resume_file' in request.FILES:
            info.resume_file = request.FILES['resume_file']
            info.save()
            return Response({"detail": "File uploaded successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def download_resume(self, request, *args, **kwargs):
        info = BasicInformation.objects.first()
        if info and info.resume_file:
            return Response({"file_url": info.resume_file.url}, status=status.HTTP_200_OK)
        return Response({"detail": "No file uploaded"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['put'])
    def save_basic_information(self, request, *args, **kwargs):
        info = BasicInformation.objects.first()
        if not info:
            return Response({"detail":"Basic information not found"}, status=status.HTTP_404_NOT_FOUND)        
        serializer = self.get_serializer(info, data=request.data, partial=True)        
        if serializer.is_valid():            
            serializer.save()            
            return Response(serializer.data, status=status.HTTP_200_OK)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-from_date')
    serializer_class = ExperienceSerializer

    @action(detail=False, methods=['post'], url_path='save-experience')
    def save_experience(self, request):
        data = {
            "company": request.data.get("company"),
            "job_title": request.data.get("job_title"),
            "job_role": request.data.get("job_role"),
            "from_date": request.data.get("from_date"),
            "to_date": request.data.get("to_date"),
        }

        serializer = ExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer