from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserVenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_venues')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue_users')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is a regular at {self.venue}"

    class Meta:
        """Sets user and venue to unique together."""
        unique_together = ("user", "venue")
