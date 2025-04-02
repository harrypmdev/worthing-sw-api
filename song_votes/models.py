from django.db import models

from songs.models import Song
from votes.models import Vote


class SongVote(Vote):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "song")
