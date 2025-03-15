from django.db import models

from base_content.models import BaseContent


class Post(BaseContent):
    content = models.TextField()
    songs = models.ManyToManyField('songs.Song', related_name='posts', blank=True)
