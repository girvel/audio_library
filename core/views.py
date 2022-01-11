from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Track


def index(request):
    return render(request, 'index.html', {
        'tracks': Track.objects.all()
    })
