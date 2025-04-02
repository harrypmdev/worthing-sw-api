from django.db import models
from django.contrib.auth.models import User


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    downvote = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.id}: "
            + ("downvote" if self.downvote else "upvote")
            + f" on {self.user.username}'s post"
        )
