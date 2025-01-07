from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Contact

class ContactAPITestCase(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

        # Valid payload
        self.valid_payload = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "message": "This is a test message."
        }

        # Invalid payloads
        self.invalid_payload_missing_fields = {
            "name": "John Doe",
            "email": "johndoe@example.com"
        }

        self.invalid_payload_invalid_email = {
            "name": "John Doe",
            "email": "invalid-email",
            "message": "This is a test message."
        }

    def test_create_contact_valid(self):
        """Test creating a contact with valid payload."""
        response = self.client.post('/api/contact/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Your message has been sent successfully!")
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().name, self.valid_payload['name'])

    def test_create_contact_missing_fields(self):
        """Test creating a contact with missing required fields."""
        response = self.client.post('/api/contact/', self.invalid_payload_missing_fields, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)

    def test_create_contact_invalid_email(self):
        """Test creating a contact with an invalid email address."""
        response = self.client.post('/api/contact/', self.invalid_payload_invalid_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_create_contact_empty_payload(self):
        """Test creating a contact with an empty payload."""
        response = self.client.post('/api/contact/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('email', response.data)
        self.assertIn('message', response.data)
