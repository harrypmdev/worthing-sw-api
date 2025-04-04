"""Django models file that defines the ORM models for the Venue and
UserVenue entities.

Both are included in the venues app as UserVenue is a junction table
for the many-to-many relationship between User and Venue.
"""

from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    """Defines a single Venue.

    Fields:
    name: models.CharField -- the name of the venue.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its name field.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string to represent the Venue model by its name."""
        return self.name


class UserVenue(models.Model):
    """Defines the UserVenue model, a junction table connecting User and Venue.

    Fields:
    user: models.ForeignKey -- the foreign key that links UserVenue to the User model.
    venue: models.ForeignKey -- the foreign key that links UserVenue to the Venue model.
    created_at: models.DateTimeField -- the date and time of creation.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its user and venue.

    A django model Meta class sets the user and venue as unique together.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_venues')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue_users')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is a regular at {self.venue}"

    class Meta:
        """Sets user and venue to unique together."""
        unique_together = ("user", "venue")
