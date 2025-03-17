from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from post_votes.models import PostVote


def update_net_votes(post):
    """Recalculate and update the net_votes for a Post."""
    # Count upvotes and downvotes for the specific Post
    upvotes = PostVote.objects.filter(post=post, downvote=False).count()
    downvotes = PostVote.objects.filter(post=post, downvote=True).count()
    post.net_votes = upvotes - downvotes
    post.save()


@receiver(post_save, sender=PostVote)
def handle_post_vote_save(sender, instance, created, **kwargs):
    """Update net_votes on vote creation or update."""
    update_net_votes(instance.post)


@receiver(post_delete, sender=PostVote)
def handle_post_vote_delete(sender, instance, **kwargs):
    """Update net_votes on vote deletion."""
    update_net_votes(instance.post)
