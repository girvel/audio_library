from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from django.forms import model_to_dict
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Track


def index(request):
    return render(request, 'index.html')


# Sketch for future:
# class ExtendedEncoder(AutomatedEncoder):
#     @handler
#     def handle_model(self, o: Model):
#         return model_to_dict(o)

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)

        if isinstance(o, FieldFile):
            return o.url

        return super().default(o)


def get_tracks(request):
    return JsonResponse({
        'tracks': list(Track.objects.all()),
    }, encoder=ExtendedEncoder)
