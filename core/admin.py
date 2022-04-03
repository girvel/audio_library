from django.contrib import admin

from .forms import TrackForm
from .models import Track

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    form = TrackForm

# admin.site.register(Track)
