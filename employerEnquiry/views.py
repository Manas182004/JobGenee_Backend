from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Enquiry
from .serializers import EnquirySerializer

@api_view(['POST'])
def submit_enquiry(request):
    if request.method == 'POST':
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Enquiry submitted successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
