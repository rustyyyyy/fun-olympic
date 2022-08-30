from django.urls import path
from .views import HomeView, VideoDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
]
