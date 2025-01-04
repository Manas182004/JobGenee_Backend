# dashboard/tests.py


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import BasicInformation, Education, Certification

class ResumeAPITests(TestCase):
    def setUp(self):
        """Set up the test environment and initialize the API client."""
        self.client = APIClient()
        self.resume_upload_url = '/api/upload-resume/'  # Adjust this URL to your endpoint
        self.basic_info_url = '/api/basic-information/'
        self.education_url = '/api/education/'
        self.certifications_url = '/api/certifications/'
        
        # Example payloads
        self.basic_info_payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890"
        }
        self.education_payload = {
            "degree": "B.Sc. in Computer Science",
            "institution": "ABC University",
            "start_date": "2015-09-01",
            "end_date": "2019-06-01",
            "grade": "A"
        }
        self.certification_payload = {
            "name": "AWS Certified Solutions Architect",
            "organization": "Amazon Web Services",
            "date_earned": "2023-01-15"
        }

    def test_upload_resume(self):
        """Test uploading a resume and verifying the response."""
        with open('sample_resume.pdf', 'rb') as resume_file:
            response = self.client.post(self.resume_upload_url, {'resume': resume_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

    def test_create_basic_information(self):
        """Test creating a BasicInformation record."""
        response = self.client.post(self.basic_info_url, self.basic_info_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BasicInformation.objects.count(), 1)
        self.assertEqual(BasicInformation.objects.first().email, self.basic_info_payload['email'])

    def test_create_education(self):
        """Test creating an Education record."""
        response = self.client.post(self.education_url, self.education_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Education.objects.count(), 1)
        self.assertEqual(Education.objects.first().degree, self.education_payload['degree'])

    def test_create_certification(self):
        """Test creating a Certification record."""
        response = self.client.post(self.certifications_url, self.certification_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Certification.objects.count(), 1)
        self.assertEqual(Certification.objects.first().name, self.certification_payload['name'])

    def test_invalid_basic_information(self):
        """Test validation for BasicInformation endpoint."""
        invalid_payload = {"first_name": "", "email": "not-an-email"}
        response = self.client.post(self.basic_info_url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('first_name', response.data)