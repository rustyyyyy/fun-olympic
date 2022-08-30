from main.settings import TIME_ZONE
from operator import mod
from django.db import models
from users.models import CustomUser
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    user = models.ForeignKey(CustomUser,
                on_delete= models.CASCADE,related_name='post_aurthor')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    video_link = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
