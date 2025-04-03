"""Django models file that defines the ORM model for the Comment entity."""

from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Comment(models.Model):
    """Defines a single Comment, a model with a many-to-one relationship
    with both User and Post.

    Fields:
    user: models.ForeignKey -- the foreign key that links Comment to a single User instance.
    post: models.ForeignKey -- the foreign key that links Comment to a single Post instance.
    created_at: models.DateTimeField -- the date and time of creation.
    updated_at: models.DateTimeField -- the date and time of the last update.
    content: models.TextField -- the text content of the Comment.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its id and content.

    A django model Meta class sets the default ordering as most recently created first.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=300)

    class Meta:
        """Set the default ordering as most recently created first."""

        ordering = ["-created_at"]

    def __str__(self):
        """Return a string to represent the Profile model.
        Returns the id and first 10 characters of the content.
        """
        if len(self.content) > 10:
            return f"{self.id}: {self.content}"
        else:
            return f"{self.id}: {self.content[:10]}"
