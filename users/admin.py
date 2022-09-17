from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, EmailVerification, UserAvatar, Notification, RestPasswordRequest


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("id", "email", "username", "is_staff", "is_active", "date_joined")
    fieldsets = (
        (None, {"fields": (
                "username", "email", "password",
                "first_name", "last_name",
                "phone", "gender", "country"
                )
            }
        ),
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


class EmailVerificationAdmin(admin.ModelAdmin):
    model = EmailVerification
    list_display = [
        "user",
        "id",
        "verification_code",
        "verified",
        "created_at",
        "updated_at",
    ]
admin.site.register(EmailVerification, EmailVerificationAdmin)


admin.site.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    model = UserAvatar
    list_display = [
        "user",
        "id",
    ]


admin.site.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = [
        "user",
        "id",
    ]

@admin.register(RestPasswordRequest)
class RestPasswordRequestAdmin(admin.ModelAdmin):
    model = RestPasswordRequest
    list_display = ['user', 'is_active', 'created_at']

from django.contrib.auth.models import Group
admin.site.unregister(Group)
