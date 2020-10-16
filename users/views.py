from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    return render(request, "user/login.html")


def logout_view(request):
    pass
