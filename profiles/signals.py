"""Signals file that defines a receiver to ensure a new profile is
created for every new user.
"""

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a profile instance for every new user."""
    if created:
        Profile.objects.create(user=instance)
