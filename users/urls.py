from django.urls import path
from users.views import (
    EmailVerify, SignupView, LoginView,
    LogoutView, ForgotPasswordView, ProfileView)


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("emailverify/<int:pk>", EmailVerify.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-reset/", ForgotPasswordView.as_view(), name="forgotpassword"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
