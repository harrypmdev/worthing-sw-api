from django.db import models

from base_content.models import BaseContent


class Song(BaseContent):
    audio_file = models.FileField(upload_to='songs/')
    artist_name = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.title} by {self.artist_name}'
