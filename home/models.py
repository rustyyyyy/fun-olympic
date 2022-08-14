# from main.settings import TIME_ZONE
# from operator import mod
# from django.db import models
# from users.models import CustomUser
# # Create your models here.

# class Aurthor(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='aurthor_user')

#     def __str__(self):
#         return str(self.user.email)


# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(Aurthor, on_delete= models.CASCADE,related_name='post_aurthor')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     # status = models.IntegerField(choices=STATUS, default=0)

#     upload_date = models.DateTimeField(default=TIME_ZONE.now)
#     video = models.FileField(upload_to='')

