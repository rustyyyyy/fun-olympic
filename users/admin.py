from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, EmailVerification, UserAvatar


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "username", "is_staff", "is_active", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(EmailVerification)
class EmailVerification(admin.ModelAdmin):
    model = EmailVerification
    list_display = [
        "user",
        "id",
        "verification_code",
        "verified",
        "created_at",
        "updated_at",
    ]

@admin.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    model = UserAvatar
    list_display = [
        "user",
        "id",
    ]
