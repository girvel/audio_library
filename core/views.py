from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'tracks': [
            {
                'name': 'Evening Wear',
                'author': 'Mindless Self Indulgence',
                'path': 'audio/Mindless Self Indulgence - Evening Wear.mp3'
            }
        ]
    })
