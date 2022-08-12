from django.urls import path
from users.views import EmailVerify, SignupView, LoginView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("emailverify/<int:pk>", EmailVerify.as_view(), name="signup")
]