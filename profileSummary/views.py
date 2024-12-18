from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ProfileSummary
from .serializers import ProfileSummarySerializer

class ProfileSummaryView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile_summary = ProfileSummary.objects.get(user=request.user)
            serializer = ProfileSummarySerializer(profile_summary)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProfileSummary.DoesNotExist:
            return Response({"summary": ""}, status=status.HTTP_200_OK)  # Return empty if not found

    def post(self, request):
        try:
            profile_summary, created = ProfileSummary.objects.get_or_create(user=request.user)
            serializer = ProfileSummarySerializer(profile_summary, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)