# dashboard/views.py




from rest_framework import viewsets
from .models import BasicInformation, Certification, Education, Experience, Language, Project
from .serializers import (BasicInformationSerializer, CertificationSerializer,
                          EducationSerializer, ExperienceSerializer,
                          LanguageSerializer, ProjectSerializer)

class BasicInformationViewSet(viewsets.ModelViewSet):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer

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