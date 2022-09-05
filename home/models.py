from statistics import mode
from turtle import update
from unicodedata import category
from main.settings import TIME_ZONE
from operator import mod
from django.db import models
from users.models import CustomUser
from embed_video.fields import EmbedVideoField
from config.models import Categories


class Video(models.Model):
    user = models.ForeignKey(CustomUser,
                on_delete= models.CASCADE,related_name='user_video')
    
    category = models.ForeignKey(Categories,
        on_delete=models.DO_NOTHING, related_name='category_video', null=True)

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    video_link = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(CustomUser,
                on_delete= models.CASCADE,related_name='user_comment', blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video.title


class Views(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE
    ,related_name='video_views')
    count = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.count)
    class Meta:
        verbose_name_plural = "Views"


class Like(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE,related_name='video_like')
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_like = models.BooleanField(default=False)
    count = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.video.title)
