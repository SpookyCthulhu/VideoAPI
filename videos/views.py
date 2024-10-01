from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Video
from .serializers import VideoSerializer

class VideoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDownloadView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            video = Video.objects.get(pk=pk)
            response = HttpResponse(video.video_file, content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{video.video_file.name}"'
            return response
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
