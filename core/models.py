from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=255, help_text='Track\'s name')
    author = models.CharField(max_length=255, help_text='Track\'s author')
    path = models.CharField(max_length=255, help_text='Path to track')

    def __str__(self):
        return f"{self.author} - {self.name}"
