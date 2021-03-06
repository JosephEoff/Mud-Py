from django.shortcuts import render

# Create your views here.
from django.urls import path

from . import views

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the zones index.")
