from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StaticImage
from .serializer import StaticImageSerializer


class StaticImageView(APIView):

    def get(self, request, pk=None):
        all_image = get_object_or_404(StaticImage, pk=pk)
        serializer = StaticImageSerializer(
            all_image, many=False, context={"request": request}
        )

        return Response(serializer.data['image'], status=status.HTTP_200_OK)

