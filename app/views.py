from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import ShortLink
from .serializers import ShortLinkSerializer

class ShortenURLView(APIView):
    def post(self, request):
        url = request.data.get("url")

        if not url:
            return Response(
                {"error": "URL is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Add http:// if scheme is missing
        # if not url.startswith(("http://", "https://")):
        #     url = "http://" + url

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url


        short_link = ShortLink.objects.create(original_url=url)
        serializer = ShortLinkSerializer(
            short_link,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def redirect_view(request, code):
    link = get_object_or_404(ShortLink, short_code=code)
    return redirect(link.original_url)
