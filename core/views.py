from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Track


def index(request):
    return render(request, 'index.html', {
        'tracks': Track.objects.all()
    })

def by_author(request, author_name):
    return render(request, 'author.html', {
        'author': author_name,
        'tracks': Track.objects.filter(author=author_name)
    })

def by_name(request, author_name, track_name):
    return render(request, 'track.html', {
        'author': author_name,
        'track': track_name,
        'tracks': Track.objects.filter(author=author_name, name=track_name)
    })
