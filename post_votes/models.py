from django.db import models

from posts.models import Post
from votes.models import Vote


class PostVote(Vote):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "post")
