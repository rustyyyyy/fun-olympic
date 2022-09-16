from email.mime import image
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from turtle import title, update
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


class Features(models.Model):
    title = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='feat/images/')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Features"


class Schedule(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()
    teams = models.CharField(max_length=224)

    def __str__(self):
        return str(self.category.name)

class Gallery(models.Model):
    title = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to='gallery/images/')

    def __str__(self):
        return str(self.title)

class Athelete(models.Model):
    name = models.CharField(max_length=225, null=True)
    description = models.TextField(max_length=225, null=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    dob = models.CharField(max_length=255, null=True)
    firstgame = models.DateField(null=True)
    participants = models.CharField(max_length=255, null=True)
    team = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='athelete/images/')

    def __str__(self):
        return str(self.name)


class News(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"