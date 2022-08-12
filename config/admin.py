from django.contrib import admin

from config.models import  StaticImage



@admin.register(StaticImage)
class StaticImageAdmin(admin.ModelAdmin):
    model = StaticImage
    list_display = ["name", "id", "created_at", "updated_at"]
