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

#BasicInformation views 
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

#Certification views
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    
    @action(detail=False, methods=['post'], url_path='create-certification')
    def create_certification(self, request):
        data = {
            "name": request.data.get("name"),
            "link": request.data.get("link"),
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date"),
        }
        """POST: Add a new certification record."""
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='update-certification')
    def update_certification(self, request, pk=None):
        data = {
            "name": request.data.get("name"),
            "link": request.data.get("link"),
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date"),
        }
        """PUT: Update an existing certification record."""
        certification = Certification.objects.filter(pk=pk).first()
        if not certification:
            return Response({"error": "Certification not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CertificationSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='destroy-certification')
    def destroy_certification(self, request, pk=None):
        """DELETE: Remove an certification record by primary key."""
        certification = Certification.objects.filter(pk=pk).first()
        if not certification:
            return Response({"error": "Certification not found."}, status=status.HTTP_404_NOT_FOUND)
        certification.delete()
        return Response({"message": "Certification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

#Education views
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    @action(detail=False, methods=['post'], url_path='create-education')
    def create_education(self, request):
        data = {
            "institution": request.data.get("institution"),
            "degree": request.data.get("degree"),
            "field_of_study": request.data.get("field_of_study"),
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date"),
        }
        """POST: Add a new education record."""
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='update-education')
    def update_education(self, request, pk=None):
        data = {
            "institution": request.data.get("institution"),
            "degree": request.data.get("degree"),
            "field_of_study": request.data.get("field_of_study"),
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date"),
        }
        """PUT: Update an existing education record."""
        education = Education.objects.filter(pk=pk).first()
        if not education:
            return Response({"error": "Education not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = EducationSerializer(education, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='destroy-education')
    def destroy_education(self, request, pk=None):
        """DELETE: Remove an education record by primary key."""
        education = Education.objects.filter(pk=pk).first()
        if not education:
            return Response({"error": "Education not found."}, status=status.HTTP_404_NOT_FOUND)
        education.delete()
        return Response({"message": "Education deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

#Experience views
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
    
    @action(detail=False, methods=['put'], url_path='update-experience')
    def update_experience(self, request, pk=None):
        data = {
            "company": request.data.get("company"),
            "job_title": request.data.get("job_title"),
            "job_role": request.data.get("job_role"),
            "from_date": request.data.get("from_date"),
            "to_date": request.data.get("to_date"),
        }
        """PUT: Update an existing experience record."""
        experience = Experience.objects.filter(pk=pk).first()
        if not experience:
            return Response({"error": "Experience not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExperienceSerializer(experience, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='destroy-experience')
    def destroy_experience(self, request, pk=None):
        """DELETE: Remove an experience record by primary key."""
        experience = Experience.objects.filter(pk=pk).first()
        if not experience:
            return Response({"error": "Experience not found."}, status=status.HTTP_404_NOT_FOUND)
        experience.delete()
        return Response({"message": "Experience deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

#Language views    
class LanguageViewSet(viewsets.ModelViewSet):
    """ViewSet for managing languages"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
    @action(detail=False, methods=['post'], url_path='create-language')
    def create_language(self, request):
        
        """POST: Add a new language record."""
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='update-language')
    def update_language(self, request, pk=None):
        
        """PUT: Update an existing language record."""
        language = Language.objects.filter(pk=pk).first()
        if not language:
            return Response({"error": "language not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='destroy-language')
    def destroy_language(self, request, pk=None):
        """DELETE: Remove an language record by primary key."""
        language = Language.objects.filter(pk=pk).first()
        if not language:
            return Response({"error": "Language not found."}, status=status.HTTP_404_NOT_FOUND)
        language.delete()
        return Response({"message": "Language deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

#Project views
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @action(detail=False, methods=['post'], url_path='create-project')
    def create_project(self, request):
        data = {
            "project_name": request.data.get("project_name"),
            "description": request.data.get("description"),
            "timeline": request.data.get("timeline"),
            "project_link": request.data.get("project_link"),
        }
        """POST: Add a new project record."""
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='update-project')
    def update_project(self, request, pk=None):
        data = {
            "project_name": request.data.get("project_name"),
            "description": request.data.get("description"),
            "timeline": request.data.get("timeline"),
            "project_link": request.data.get("project_link"),
        }
        """PUT: Update an existing project record."""
        project = Project.objects.filter(pk=pk).first()
        if not project:
            return Response({"error": "project not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='destroy-project')
    def destroy_project(self, request, pk=None):
        """DELETE: Remove an project record by primary key."""
        project = Project.objects.filter(pk=pk).first()
        if not project:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    