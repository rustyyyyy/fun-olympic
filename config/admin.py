from django.contrib import admin
from config.models import  StaticImage, Categories


class StaticImageAdmin(admin.ModelAdmin):
    model = StaticImage
    list_display = ["name", "id", "created_at", "updated_at"]
admin.site.register(StaticImage, StaticImageAdmin)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'id']