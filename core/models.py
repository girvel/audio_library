from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=255, help_text='Track\'s name')
    author = models.CharField(max_length=255, help_text='Track\'s author')
    file = models.FileField(upload_to='core/static/audio', help_text='Track file')

    def __str__(self):
        return f"{self.author} - {self.name}"
