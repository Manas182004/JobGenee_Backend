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
router.register(r'certifications', CertificationViewSet)
router.register(r'education', EducationViewSet)
# router.register(r'experience', ExperienceViewSet, basename='experience')
experience_list = ExperienceViewSet.as_view({'get': 'list'})
save_experience = ExperienceViewSet.as_view({'post': 'save_experience'})
router.register(r'languages', LanguageViewSet)
router.register(r'projects', ProjectViewSet)

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include routes from DefaultRouter
    path('experience/', experience_list, name='experience-list'),
    path('experience/save/', save_experience, name='experience-save'),  
    path('resume/extract/', extract_resume_data, name='extract_resume_data'),
]

