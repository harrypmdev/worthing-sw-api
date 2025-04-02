"""Django models file that defines the ORM model for the Post entity."""

from django.db import models

from base_content.models import BaseContent
from songs.models import Song


class Post(BaseContent):
    """Defines a single Post, optionally with a linked Song.
    Inherits from BaseContent, a class that defines fields shared between Song
    and Post.

    Fields:
    content: models.TextField -- the text content of the post.
    song: models.ForeignKey -- the foreign key optionally linking a Song to this post.
    """
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, blank=True, null=True)
