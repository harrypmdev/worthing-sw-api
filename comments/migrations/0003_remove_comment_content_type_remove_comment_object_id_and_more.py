# Generated by Django 4.2 on 2025-03-17 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_remove_post_songs_post_net_votes_post_song"),
        ("comments", "0002_comment_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="object_id",
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="posts.post"
            ),
            preserve_default=False,
        ),
    ]
