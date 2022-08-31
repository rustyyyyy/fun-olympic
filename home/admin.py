from django.contrib import admin
from .models import Video, Views, Comment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = [
        "title",
        "user",
        "id"
    ]

@admin.register(Views)
class ViewsAdmin(admin.ModelAdmin):
    model = Video
    list_display = [
        "count",
        "video",
        "id"
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = [
        "video",
        "user",
        "created_at",
        "id"
    ]
