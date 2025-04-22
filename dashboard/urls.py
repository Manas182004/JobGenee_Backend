# dashboard/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import spacy
from .views import (
    BasicInformationViewSet,
    CertificationViewSet,
    EducationViewSet,
    ExperienceViewSet,
    LanguageViewSet,
    ProjectViewSet,
)

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Endpoint for extracting resume data
@api_view(['POST'])
def extract_resume_data(request):
    file = request.FILES.get('resume')
    if not file:
        return Response({"error": "No file uploaded."}, status=400)
    
    try:
        text = file.read().decode('utf-8')  # Assuming plain text file
    except UnicodeDecodeError:
        return Response({"error": "Unable to decode the file. Ensure it is a plain text file."}, status=400)
    
    doc = nlp(text)
    extracted_data = {
        'entities': [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    }
    return Response(extracted_data)

# Create DefaultRouter and register viewsets
router = DefaultRouter()
router.register(r'basic-information', BasicInformationViewSet, basename='basicinformation')

#Certification
certification = CertificationViewSet.as_view({'get': 'list'})
create_certification = CertificationViewSet.as_view({'post': 'create_certification'})
update_certification = CertificationViewSet.as_view({'put': 'update_certification'})
destroy_certification = CertificationViewSet.as_view({'delete': 'destroy_certification'})

#experience
experience_list = ExperienceViewSet.as_view({'get': 'list'})
save_experience = ExperienceViewSet.as_view({'post': 'save_experience'})
update_experience = ExperienceViewSet.as_view({'put': 'update_experience'})
destroy_experience = ExperienceViewSet.as_view({'delete': 'destroy_experience'})

#education
education = EducationViewSet.as_view({'get': 'list'})
create_education = EducationViewSet.as_view({'post': 'create_education'})
update_education = EducationViewSet.as_view({'put': 'update_education'})
destroy_education = EducationViewSet.as_view({'delete': 'destroy_education'})

#language
language = LanguageViewSet.as_view({'get': 'list'})
create_language = LanguageViewSet.as_view({'post': 'create_language'})
update_language = LanguageViewSet.as_view({'put': 'update_language'})
destroy_language = LanguageViewSet.as_view({'delete': 'destroy_language'})

#project
project = ProjectViewSet.as_view({'get': 'list'})
create_project = ProjectViewSet.as_view({'post': 'create_project'})
update_project = ProjectViewSet.as_view({'put': 'update_project'})
destroy_project = ProjectViewSet.as_view({'delete': 'destroy_project'})


# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include routes from DefaultRouter
    
    #experience
    path('experience/', experience_list, name='experience-list'),
    path('experience/save/', save_experience, name='experience-save'),
    path('experience/update/<int:pk>/', update_experience, name='update-experience'),
    path('experience/destroy/<int:pk>/', destroy_experience, name='destroy-experience'),
    
    #education
    path('education/', education, name='list-education'),
    path('education/create/', create_education, name='create-education'),  
    path('education/update/<int:pk>/', update_education, name='update-education'),
    path('education/destroy/<int:pk>/', destroy_education, name='destroy-education'),
    
    #language
    path('language/', language, name='list-language'),
    path('language/create/', create_language, name='create-language'),
    path('language/update/<int:pk>/', update_language, name='update-language'),
    path('language/destroy/<int:pk>/', destroy_language, name='destroy-language'),
    
    #certification
    path('certification/', certification, name='list-certification'),
    path('certification/create/', create_certification, name='create-certification'),  
    path('certification/update/<int:pk>/', update_certification, name='update-certification'),
    path('certification/destroy/<int:pk>/', destroy_certification, name='destroy-certification'),
    
    #project
    path('project/', project, name='list-project'),
    path('project/create/', create_project, name='create-project'),  
    path('project/update/<int:pk>/', update_project, name='update-project'),
    path('project/destroy/<int:pk>/', destroy_project, name='destroy-project'),

    path('resume/extract/', extract_resume_data, name='extract_resume_data'),
]

