"""Signals file that defines receivers to ensure the Song net_votes field
is always up to date.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from song_votes.models import SongVote


def update_net_votes(song):
    """Recalculate and update the net_votes for a Song."""
    # Count upvotes and downvotes for the specific Song
    upvotes = SongVote.objects.filter(song=song, downvote=False).count()
    downvotes = SongVote.objects.filter(song=song, downvote=True).count()
    song.net_votes = upvotes - downvotes
    song.save()


@receiver(post_save, sender=SongVote)
def handle_song_vote_save(sender, instance, created, **kwargs):
    """Update net_votes on vote creation or update."""
    update_net_votes(instance.song)


@receiver(post_delete, sender=SongVote)
def handle_song_vote_delete(sender, instance, **kwargs):
    """Update net_votes on vote deletion."""
    update_net_votes(instance.song)
