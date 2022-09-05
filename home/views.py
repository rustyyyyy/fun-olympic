from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Video, Views, Comment, Like
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

        title = "Similar"
        videos = Video.objects.filter(
            category=video.category
        ).exclude(id=video.id)[:3]
        if not videos.exists():
            title = "Recent"
            videos = Video.objects.all().order_by('-id')[:3]

        comments = Comment.objects.filter(video=video)

        like = Like.objects.filter(
            video=video, is_like=True).count()

        dislike = Like.objects.filter(
            video=video, is_like=False).count()

        context = {
            'video': video,
            'view_count': count,
            'videos': videos,
            'comments': comments,
            'form': form,
            'like': like,
            'dislike': dislike,
            'title': title,
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

class likeView(View):
    def post(self, request, pk=None):
        user = request.user

        video = get_object_or_404(Video, id=pk)
        like = Like.objects.filter(user=user, video=video)
        if not like.exists():
            add_like = Like.objects.create(
                user=user,
                video=get_object_or_404(Video, id=pk),
                is_like=True
            )
            add_like.save()
        else:
            video_like = Like.objects.get(
                video=video,
                user=user
            )
            video_like.is_like = True
            video_like.save()
        
        like = Like.objects.filter(
            video=video, is_like=True).count()
        context = {
            'like':like
        }
        return render(request, 'home/video/like.html', context)


class DislikeView(View):
    def post(self, request, pk=None):
        user = request.user

        video = get_object_or_404(Video, id=pk)
        like = Like.objects.filter(user=user, video=video)
        if not like.exists():
            add_like = Like.objects.create(
                user=user,
                video=get_object_or_404(Video, id=pk),
                is_like=False
            )
            add_like.save()
        else:
            video_like = Like.objects.get(
                video=video,
                user=user
            )
            video_like.is_like = False
            video_like.save()
        
        like = Like.objects.filter(
            video=video, is_like=False).count()
        context = {
            'dislike':like, 
        }
        return render(request, 'home/video/dislike.html', context)
