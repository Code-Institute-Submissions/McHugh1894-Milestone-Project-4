from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home(request):
    """ This view returns the index page"""

    return render(request, 'home/index.html')


