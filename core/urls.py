from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<author_name>', views.by_author, name='author'),
    path('<author_name>/<track_name>', views.by_name, name='track'),
]
