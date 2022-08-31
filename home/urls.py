from django.urls import path
from .views import HomeView, VideoDetailView, VideoAddView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('<int:pk>/add/', VideoAddView.as_view(), name="video-add"),
]
