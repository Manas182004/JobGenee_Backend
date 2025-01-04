# dashboard/urls.py




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (BasicInformationViewSet, CertificationViewSet, EducationViewSet,
                    ExperienceViewSet, LanguageViewSet, ProjectViewSet)
import spacy
from rest_framework.decorators import api_view
from rest_framework.response import Response

nlp = spacy.load('en_core_web_sm')  # Load SpaCy model

@api_view(['POST'])
def extract_resume_data(request):
    file = request.FILES['resume']
    text = file.read().decode('utf-8')
    doc = nlp(text)
    extracted_data = {
        'entities': [{
            'text': ent.text,
            'label': ent.label_
        } for ent in doc.ents]
    }
    return Response(extracted_data)

router = DefaultRouter()
router.register(r'basic-information', BasicInformationViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]