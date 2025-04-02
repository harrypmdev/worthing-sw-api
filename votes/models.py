"""Django models file that defines an abstract class, Vote,
from which PostVote and SongVote models inherit.
"""

from django.db import models
from django.contrib.auth.models import User


class Vote(models.Model):
    """Defines the Vote class, an abstract model class which defines
    fields shared by both the SongVote and PostVote model.

    Fields:
    user: models.ForeignKey -- the foreign key that links Vote children
                               to a single User instance.
    created_at: models.DateTimeField -- the date and time of creation.
    downvote: models.BooleanField -- whether this vote is a downvote or not. True
                                     for a downvote, false for an upvote.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its id, downvote status and user.

    A django model Meta class defines the class as abstract and default ordering.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    downvote = models.BooleanField(default=False)

    class Meta:
        """Defines the class as abstract and set default ordering to created at."""

        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        """Return a string to summarise the class by its id, user and downvote status."""
        return (
            f"{self.id}: "
            + ("downvote" if self.downvote else "upvote")
            + f" on {self.user.username}'s post"
        )
