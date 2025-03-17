from django.db import models

from base_content.models import BaseContent
from songs.models import Song


class Post(BaseContent):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, blank=True, null=True)
    net_votes = models.IntegerField(default=0)
