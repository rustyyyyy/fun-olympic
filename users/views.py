import time
import os
from pathlib import Path
from urllib import parse

import environ
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from users.forms import (CountryForm, CustomUserCreationForm, GenderForm,
                         RegisterForm)
from users.helper import captcha_validation, email_verification
from users.models import (CustomUser, EmailVerification, RestPasswordRequest,
                          UserAvatar)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)

secret = env("secret")
site_key = env("site_key")


class SignupView(View):
    def get(self, request):
        return render(
            request,
            "auth/index.html",
            {
                "form": CustomUserCreationForm,
                "formm": RegisterForm,
                "countryform": CountryForm,
                "site_key": site_key,
                "gender_form": GenderForm,
            },
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        recaptcha_response = request.POST.get("g-recaptcha-response")

        if captcha_validation(recaptcha_response, secret):
            if form.is_valid():
                email = form.data["email"]
                form.save()

                verification = email_verification(email)

                if verification:
                    return redirect(f"/emailverify/{verification}")
                return render(
                    request,
                    "auth/index.html",
                    {"message": "Error in email verification.", "site_key": site_key},
                )

            return render(
                request,
                "auth/index.html",
                {"form": form, "formm": RegisterForm, "site_key": site_key},
            )
        return render(
            request,
            "auth/index.html",
            {"message": "Invalid reCAPTCHA. Please try again.", "site_key": site_key},
        )


class EmailVerify(View):
    def get(self, request, pk=None):
        referer = request.META.get("HTTP_REFERER")
        path = parse.urlparse(referer).path

        user = get_object_or_404(EmailVerification, pk=pk)
        email = user.user.email

        if path == "/signup/":
            return render(request, "auth/two-steps.html", {"email": email})
        return redirect("/")

    def post(self, request, pk=None):
        try:
            code = request.POST.get("code")
            user = get_object_or_404(EmailVerification, pk=pk)
            email = user.user.email

            if user.verification_code == int(code):
                user.verified = True
                user.save()

                time.sleep(1)
                return redirect("/")

            return render(
                request,
                "auth/two-steps.html",
                {"message": "Incorrect Otp", "email": email},
            )

        except Exception:
            return render(
                request,
                "auth/two-steps.html",
                {"message": "Error occured while verification.", "email": email},
            )


class LoginView(View):
    def get(self, request):
        return render(
            request,
            "registration/login.html",
        )

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user.is_staff != True:
                try:
                    email_verify = get_object_or_404(EmailVerification, user=user)

                    try:
                        reset_password_user = get_object_or_404(
                            RestPasswordRequest, user=user
                        )

                        if reset_password_user.is_active == True:
                            logout(request)
                            return redirect(f"/reset-password/?email={username}")
                    except Exception:
                        pass

                    if email_verify.verified != True:
                        logout(request)
                        messages.error(
                            request, "Verify your email by clicking forgot password"
                        )
                        return render(request, "registration/login.html")
                except Exception:
                    messages.error(
                        request, "Verify your email by clicking forgot password"
                    )
                    return render(request, "registration/login.html")

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

        return render(request, "registration/login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, "auth/password-reset.html")

    def post(self, request):
        email = request.POST.get("email")

        try:
            user = get_object_or_404(CustomUser, email=email)

            qs = RestPasswordRequest.objects.filter(user=user)
            if not qs.exists():
                RestPasswordRequest.objects.create(user=user)

            messages.success(
                request, "Password reset sucessfully requested! try to login shortly"
            )
        except Exception:
            messages.error(request, "Invalid email")

        return render(request, "auth/password-reset.html")


class ProfileView(View):
    def get(self, request):
        user = request.user

        context = {
            "form": CountryForm({"country": user.country}),
            "gender_form": GenderForm({"gender": user.gender}),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
        }
        return render(request, "home/profile.html", context)

    def post(self, request):
        data = request.POST
        user = request.user
        file = request.FILES.get("avatar")

        if file:
            user_avatar = UserAvatar.objects.filter(user=user)
            if user_avatar.exists():
                user_avatar = user_avatar[0]
                user_avatar.avatar = file
                user_avatar.save()
            else:
                UserAvatar.objects.create(user=user, avatar=file)

        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.phone = data.get("phone")
        user.username = data.get("username")
        user.gender = data.get("gender")
        user.country = data.get("country")
        user.save()

        return redirect(request.META["HTTP_REFERER"])
        # return render(request, 'home/profile.html', {})


class ResetPasswordView(View):
    def get(self, request):
        email = request.GET.get("email")
        return render(request, "home/password-reset.html", {"email": email})

    def post(self, request):
        # email = request.POST.get('email')
        # try:
        #     user = get_object_or_404(CustomUser, email=email)
        #     qs = RestPasswordRequest.objects.filter(user=user)

        #     if not qs.exists():
        #         RestPasswordRequest.objects.create(user=user)

        #     messages.success(request, "Password reset sucessfully requested! try to login shortly")
        # except Exception:
        #     messages.error(request, "Invalid email")
        data = request.POST
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if password1 != password2:
            messages.error(request, "password and confirm password must match")

        if len(password1) < 8:
            messages.error(request, "password must be at least 8 characters")

        if str(request.user) == "AnonymousUser":
            try:
                user = CustomUser.objects.get(email=email)
                reset_pass = RestPasswordRequest.objects.get(user=user)

                if reset_pass.is_active:
                    reset_pass.is_active = False
                    reset_pass.save()

                    user.set_password(password1)
                    user.save()
                    messages.success(request, "password changed sucessfully")
                    return redirect("/login/")

            except Exception:
                messages.error(request, "password request not sucessful")

        return render(request, "home/password-reset.html")
