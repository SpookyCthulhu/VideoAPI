from django.urls import path
from .views import VideoUploadView, VideoDownloadView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('download/<int:pk>/', VideoDownloadView.as_view(), name='video-download'),
]
