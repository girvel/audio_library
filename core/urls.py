from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/tracks', views.get_tracks, name='get_tracks')
]
