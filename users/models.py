from tkinter.tix import Tree
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class EmailVerification(models.Model):
    user = models.OneToOneField(
        CustomUser, blank=False, unique=True, on_delete=models.CASCADE
    )
    verification_code = models.IntegerField()
    verified = models.BooleanField(default=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class UserAvatar(models.Model):
    user = models.OneToOneField(
        CustomUser, blank=False, unique=True, on_delete=models.CASCADE, related_name='avatar_user'
    )
    avatar = models.ImageField(upload_to ='user/avatar/')

    def __str__(self):
        return self.user.email


class Notification(models.Model):
    user = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name="user_noti")
    msg = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.user.email

class RestPasswordRequest(models.Model):
    user = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name="reset_password_user")
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
