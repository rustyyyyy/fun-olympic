from django.contrib import admin
from .models import Video 

@admin.register(Video)
class UserAvatarAdmin(admin.ModelAdmin):
    model = Video
    list_display = [
        "title",
        "user",
        "id"
    ]
