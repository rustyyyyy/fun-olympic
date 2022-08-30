from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Video


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        videos = Video.objects.all()
        context = {
            'videos': videos
        }
        return render(request, 'home/video/index.html', context)
