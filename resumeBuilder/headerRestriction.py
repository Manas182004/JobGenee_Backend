class RestrictHeadersMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        allowed_headers = ['Authorization', 'Content-Type']
        for header in request.headers.keys():
            if header not in allowed_headers:
                return Response({"error": "Forbidden header detected."}, status=status.HTTP_403_FORBIDDEN)
        return self.get_response(request)