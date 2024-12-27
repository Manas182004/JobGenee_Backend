#empregistration/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEmployerUser
from .serializers import EmployerRegistrationSerializer

class EmployerRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully Registered!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerPortalView(APIView):
    permission_classes = [IsAuthenticated, IsEmployerUser]

    def get(self, request):
        return Response({"message": "Welcome, Employer!"})