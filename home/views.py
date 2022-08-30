from re import I
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Video
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


# class HomeView(LoginRequiredMixin, View):
class HomeView(View):
    def get(self, request):
        videos = Video.objects.all()

        paginator = Paginator(videos, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj
        }
        return render(request, 'home/video/index.html', context)


class VideoDetailView(View):

    def get(self, request, pk=None):
        video = get_object_or_404(Video, id=pk)
        videos = Video.objects.all()[:3]
        context = {
            'video': video,
            'videos': videos
        }
        return render(request, 'home/video/video-detail.html', context)