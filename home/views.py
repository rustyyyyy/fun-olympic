from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Video, Views, Comment
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import CommentForm


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

        form = CommentForm()
        try:
            count = Views.objects.filter(video=video)[0]
        except Exception:
            count = Views.objects.create(video=video)

        # count.count += 1
        # count.save()

        videos = Video.objects.all().order_by('-id')[:3]
        comments = Comment.objects.filter(video=video)

        context = {
            'video': video,
            'view_count': count,
            'videos': videos,
            'comments': comments,
            'form': form,
            'pk': pk
        }
        return render(request, 'home/video/video-detail.html', context)


class VideoAddView(View):

    def post(self, request, pk=None):

        video = get_object_or_404(Video, id=pk)
        comment = request.POST.get('comment')
        if len(comment) > 1:
            new_comment = Comment.objects.create(
                video = video,
                user = request.user,
                comment = comment
            )
            new_comment.save()

        comments = Comment.objects.filter(
            video=video
        )
        context = {
            'comments': comments,
            'pk': pk
        }
        return render(request, 'home/video/comment.html', context)