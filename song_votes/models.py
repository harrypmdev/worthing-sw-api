"""Django models file that defines the ORM model for the SongVote entity."""

from django.db import models

from songs.models import Song
from votes.models import Vote


class SongVote(Vote):
    """Defines a SongVote model, a model for storing votes made on songs with
    a many-to-one relationship with Song.
    Inherits from Vote, a class that defines fields shared between SongVote
    and PostVote.

    Fields:
    song: models.ForeignKey -- the foreign key that links SongVote to the Song
                               it is a vote on.

    A django model Meta class sets the User (inherited from Vote) and Song foreign
    keys as unique together to prevent conflicts.
    """

    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        """Sets User and Song to unique together."""

        unique_together = ("user", "song")
