from django.urls import path

from .views import ViralVideoList, viral_video_detail


urlpatterns = [
    path("", ViralVideoList.as_view(), name="viral_video_list"),
    path('<uuid:pk>/', viral_video_detail,
         name='viral-video-detail'),
]