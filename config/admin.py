from django.contrib import admin
from config.models import  StaticImage


class StaticImageAdmin(admin.ModelAdmin):
    model = StaticImage
    list_display = ["name", "id", "created_at", "updated_at"]
admin.site.register(StaticImage, StaticImageAdmin)