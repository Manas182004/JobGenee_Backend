from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployerRegistrationSerializer

class EmployerRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully Registered!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
