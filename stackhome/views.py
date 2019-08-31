from django.shortcuts import render
from django.views import generic


# from .models import Appartement


# Create your views here.


def index(request):
    return render(request, 'stackhome/index.html')


def stackhome(request):
    return render(request, 'stackhome/detail.html')