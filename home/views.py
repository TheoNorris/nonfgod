from django.shortcuts import render
from .models import Artwork


def home(request):
    context = {
        'artwork': Artwork.objects.all()
    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', {'title': 'About'})