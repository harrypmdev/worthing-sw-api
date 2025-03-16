from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from posts.models import Post
from songs.models import Song
from .models import Vote


@receiver(post_save, sender=Post)
def create_vote_for_post(sender, instance, created, **kwargs):
    if created:
        Vote.objects.create(
            user=instance.user,
            content_type=ContentType.objects.get_for_model(Post),
            object_id=instance.id,
            downvote=False
        )


@receiver(post_save, sender=Song)
def create_vote_for_song(sender, instance, created, **kwargs):
    if created:
        Vote.objects.create(
            user=instance.user,
            content_type=ContentType.objects.get_for_model(Song),
            object_id=instance.id,
            downvote=False
        )
