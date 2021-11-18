from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    """ This view returns the index page"""

    return render(request, 'home/index.html')
