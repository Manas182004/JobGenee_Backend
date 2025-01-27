#empLanding/urls.py

import requests
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET'])
def get_jobs(request):
    try:
        # Replace 'http://external-api-url.com/jobpost/' with your jobpost API URL
        external_api_url = 'http://127.0.0.1:8000/jobpost/jobs/'  
        response = requests.get(external_api_url)

        # Check if the response is successful
        if response.status_code == 200:
            jobs = response.json()  # Parse the JSON response
            return Response(jobs)  # Return the data to the frontend
        else:
            return Response(
                {"error": f"Failed to fetch jobs: {response.status_code}"},
                status=response.status_code
            )
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
