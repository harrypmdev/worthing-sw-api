"""Django models file that defines the ORM model for the Follower entity."""

from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """Defines a single Comment, a model with a many-to-one relationship
    with both User and Post.

    Fields:
    user: models.ForeignKey -- the foreign key that links Follower to the User
                               the Follower belongs to.
    followed: models.ForeignKey -- the foreign key that links Follower to the User
                                   the that is being followed.
    created_at: models.DateTimeField -- the date and time of creation.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its owner user and followed user.

    A django model Meta class sets the default ordering as most recently created first, and
    sets the user and followed fields as unique together.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followed",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Set the default ordering as most recently created first, and set
        user and followed fields as unique together.
        """

        ordering = ["-created_at"]
        unique_together = ["user", "followed"]

    def __str__(self):
        """Return a string to represent the Follower model by its user and followed fields."""
        return f"{self.user} following {self.followed}"
