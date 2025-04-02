"""Django models file that defines the ORM model for the PostVote entity."""

from django.db import models

from posts.models import Post
from votes.models import Vote


class PostVote(Vote):
    """Defines a PostVote model, a model for storing votes made on posts with
    a many-to-one relationship with Post.
    Inherits from Vote, a class that defines fields shared between SongVote
    and PostVote.

    Fields:
    post: models.ForeignKey -- the foreign key that links PostVote to the Post
                               it is a vote on.

    A django model Meta class sets the User (inherited from Vote) and Post foreign
    keys as unique together to prevent conflicts.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        """Sets User and Post to unique together."""

        unique_together = ("user", "post")
