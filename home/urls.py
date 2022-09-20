from django.urls import path

from .views import (DislikeView, GalleryView, HomeView, ScheduleView, AdminStatsView,
                    VideoAddView, VideoDetailView, VideoView, likeView, AboutView, AtheletesView)

urlpatterns = [
    # nav urls
    path("", HomeView.as_view(), name="home"),
    path("gallery", GalleryView.as_view(), name="gallery"),
    path("schedule", ScheduleView.as_view(), name="schedule"),
    path("about", AboutView.as_view(), name="about"),
    path("atheletes", AtheletesView.as_view(), name="atheletes"),
    # video urls
    path("videos/", VideoView.as_view(), name="video"),
    path("videos/<int:pk>/", VideoDetailView.as_view(), name="video-detail"),
    path("videos/<int:pk>/add/", VideoAddView.as_view(), name="video-add"),
    path("videos/<int:pk>/like/add/", likeView.as_view(), name="like-add"),
    path("videos/<int:pk>/dislike/add/", DislikeView.as_view(), name="dislike-add"),
    # user analytics
    path("admin-stats/", AdminStatsView.as_view(), name="admin-stats"),

]
