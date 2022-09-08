from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from config.models import Categories

from .forms import CommentForm
from .models import Comment, Features, Like, Video, Views, Schedule, Gallery, Athelete


# class HomeView(LoginRequiredMixin, View):
class HomeView(View):
    def get(self, request):
        feat = Features.objects.all()

        context = {
            'feat': feat
        }
        return render(request, 'home/home.html', context)


class ScheduleView(LoginRequiredMixin, View):
    def get(self, request):
        data = Schedule.objects.all()
        context ={
            "obj" : data
        }
        return render(request, 'home/schedule.html', context)

class GalleryView(LoginRequiredMixin, View):
    def get(self, request):
        post = Gallery.objects.all()
        context ={
            "post": post
        }
        return render(request, 'home/gallery.html', context)


class VideoDetailView(LoginRequiredMixin, View):

    def get(self, request, pk=None):
        video = get_object_or_404(Video, id=pk)

        form = CommentForm()
        try:
            count = Views.objects.filter(video=video)[0]
        except Exception:
            count = Views.objects.create(video=video)

        count.count += 1
        count.save()

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


class VideoAddView(LoginRequiredMixin, View):

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

class likeView(LoginRequiredMixin, View):
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


class DislikeView(LoginRequiredMixin, View):
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


class VideoView(LoginRequiredMixin, View):
    def get(self, request):

        videos = Video.objects.all()

        q = self.request.GET.get('q')

        if q is not None:
            videos = Video.objects.filter(
                Q(title__icontains=q) |
                Q(category__name__contains=q)
            )

        paginator = Paginator(videos, 6)

        page_number = request.GET.get('page')
        obj = paginator.get_page(page_number)

        categories = Categories.objects.all()
        context = {
            'page_obj': obj,
            'categories' : categories
        }
        return render(request, 'home/video/index.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html', {})

class AtheletesView(View):
    def get(self, request):
        obj = Athelete.objects.all()
        return render(request, 'home/athelete.html', {'obj':obj})