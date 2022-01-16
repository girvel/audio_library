from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from .models import Track


def index(request):
    return render(request, 'index.html', {
        'tracks': Track.objects.all()
    })

def by_author(request, author_name):
    tracks = Track.objects.filter(author=author_name)

    if len(tracks) == 0:
        raise Http404(f'There is no artist named "{author_name}"')

    return render(request, 'author.html', {
        'author': author_name,
        'tracks': tracks
    })

def by_name(request, author_name, track_name):
    tracks = Track.objects.filter(author=author_name, name=track_name)

    if len(tracks) == 0:
        raise Http404(f'There is no track "{author_name} - {track_name}"')

    return render(request, 'track.html', {
        'author': author_name,
        'track': track_name,
        'tracks': Track.objects.filter(author=author_name, name=track_name)
    })
