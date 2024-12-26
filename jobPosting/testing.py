from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class JobPostingAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_job_posting(self):
        data = {
            "job_title": "Test Job",
            "job_description": "A test job description",
            "work_type": "Remote",
            "location": [{"value": "Mumbai", "label": "Mumbai"}],
            "skills": [{"value": "Python", "label": "Python"}],
            "employment_type": "Full Time",
        }
        response = self.client.post('/job-postings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
