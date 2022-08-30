import imp
from django.urls import path
from .views import StaticImageView

urlpatterns = [
    path('staticimage/<int:pk>', StaticImageView.as_view(), name="static-image")
]