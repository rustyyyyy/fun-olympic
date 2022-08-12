from django.db import models
from users.models import CustomUser

# Create your models here.
# class EmailVerification(models.Model):
#     user = models.OneToOneField(CustomUser, blank=False, unique=True, on_delete=models.CASCADE)
#     verification_code = models.IntegerField()
#     verified = models.BooleanField(default=False,blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.email

class StaticImage(models.Model):
    name = models.CharField(blank=False,max_length=250)
    image = models.ImageField(upload_to='static/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name