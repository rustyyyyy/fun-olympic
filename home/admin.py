from django.contrib import admin
from .models import(
    Video, Views, Comment, Like, Features, Schedule, Gallery,
    Athelete)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ["title", "user", "category", "id"]


@admin.register(Views)
class ViewsAdmin(admin.ModelAdmin):
    model = Video
    list_display = ["count", "video", "id"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["video", "user", "created_at", "id"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ["video", "is_like", "user", "created_at", "id"]


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    model = Features
    list_display = ["title", "id"]

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ["category", "id"]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ["title", "id"]

@admin.register(Athelete)
class AtheleteAdmin(admin.ModelAdmin):
    model = Athelete
    list_display = ["name", "id"]
