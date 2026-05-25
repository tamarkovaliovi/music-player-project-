from django.shortcuts import render
from .models import Song


def index(request):
    songs = Song.objects.all().order_by('title')
    return render(request, 'index.html', {'songs': songs})