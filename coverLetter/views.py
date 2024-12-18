from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CoverLetter
from .serializers import CoverLetterSerializer
import os

class CoverLetterUploadView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith(('.pdf', '.doc', '.docx')):
            return Response({"error": "Invalid file format. Only .pdf, .doc, and .docx are allowed."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Save file to the database
        cover_letter = CoverLetter.objects.create(user=request.user, file=file)
        return Response(CoverLetterSerializer(cover_letter).data, status=status.HTTP_201_CREATED)

class CoverLetterDownloadView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cover_letter = CoverLetter.objects.get(user=request.user)
            file_path = cover_letter.file.path
            file_name = os.path.basename(file_path)

            response = Response(open(file_path, 'rb').read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response

        except CoverLetter.DoesNotExist:
            return Response({"error": "No cover letter found for this user."}, status=status.HTTP_404_NOT_FOUND)