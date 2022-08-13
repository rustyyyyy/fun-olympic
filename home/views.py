from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home/base.html')
