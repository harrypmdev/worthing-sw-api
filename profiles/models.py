"""Django models file that defines the ORM model for the Profile entity."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Defines a single Profile, an entity with a one-to-one relationship to the
    User model to provide site-specific profile information.

    Fields:
    user: models.ForeignKey -- the foreign key that links Profile to a single User instance.
    bio: models.TextField -- a short profile bio to sum up a user's profile.
    created_at: models.DateTimeField -- the date and time of creation.
    image: models.ImageField -- the URL to the image as hosted by Cloudinary. Image upload
                                functionality handed automatically by Cloudinary middleware.

    Methods:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its related user's username.

    A django model Meta class sets the default ordering as most recently created first.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="images/", default="../guitar-logo-white_utocxc"
    )

    class Meta:
        """Set the default ordering as most recently created first."""
        ordering = ["-created_at"]

    def __str__(self):
        """Return a string to represent the Profile model."""
        return f"{self.user.username}'s Profile"
