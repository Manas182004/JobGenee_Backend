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

    # @action(detail=False, methods=['get'], url_path='list-education')
    # def list_education(self, request):
    #     """GET: Retrieve all education records."""
    #     queryset = Education.objects.all()  # No filtering by user
    #     serializer = EducationSerializer(queryset, many=True)
    #     return Response(serializer.data)

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
    """ViewSet for managing languages"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
    @action(detail=False, methods=['get'], url_path='list-language')
    def list_language(self, request, *args, **kwargs):
        """List all languages."""
        languages = self.get_queryset()
        serializer = self.get_serializer(languages, many=True)
        return Response({"language": serializer.data})
    
    @action(detail=False, methods=['post'], url_path='create-language')
    def create_language(self, request, *args, **kwargs):
        """Add a new language."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"language" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"language": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_path='update-language')
    def update_language(self, request, *args, **kwargs):
        """Update a language."""
        language = self.get_object()
        serializer = self.get_serializer(language, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"language": serializer.data}, status=status.HTTP_200_OK)
        return Response({"language": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['delete'], url_path='destroy-language')
    def destroy_language(self, request, *args, **kwargs):
        """Delete a language."""
        language = self.get_object()
        language.delete()
        return Response({"language": "Language deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer