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
# router.register(r'education', EducationViewSet, basename='education')

#experience
experience_list = ExperienceViewSet.as_view({'get': 'list'})
save_experience = ExperienceViewSet.as_view({'post': 'save_experience'})

#education
education = EducationViewSet.as_view({'get': 'list'})
create_education = EducationViewSet.as_view({'post': 'create_education'})
update_education = EducationViewSet.as_view({'put': 'update_education'})
destroy_education = EducationViewSet.as_view({'delete': 'destroy_education'})

#language
list_language = LanguageViewSet.as_view({'get': 'list_language'})
create_language = LanguageViewSet.as_view({'post': 'create_language'})
update_language = LanguageViewSet.as_view({'put': 'update_language'})
destroy_language = LanguageViewSet.as_view({'delete': 'destroy_language'})

# router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'projects', ProjectViewSet)

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include routes from DefaultRouter
    
    #experience
    path('experience/', experience_list, name='experience-list'),
    path('experience/save/', save_experience, name='experience-save'),
    
    #education
    path('education/', education, name='list-education'),
    path('education/create/', create_education, name='create-education'),  
    path('education/update/', update_education, name='update-education'),  
    path('education/destroy/', destroy_education, name='destroy-education'),
    
    #language
    path('language/list/', list_language, name='list-language'),
    path('language/create/', list_language, name='create-language'),
    path('language/update/', list_language, name='update-language'),
    path('language/destroy/', list_language, name='destroy-language'),

    path('resume/extract/', extract_resume_data, name='extract_resume_data'),
]

