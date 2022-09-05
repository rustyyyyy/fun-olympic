from django.urls import path
from .views import HomeView, VideoDetailView, VideoAddView, likeView, DislikeView, VideoView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    # video urls
    path('videos/', VideoView.as_view(), name='video'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('videos/<int:pk>/add/', VideoAddView.as_view(), name="video-add"),
    path('videos/<int:pk>/like/add/', likeView.as_view(), name="like-add"),
    path('videos/<int:pk>/dislike/add/', DislikeView.as_view(), name="dislike-add"),


]
