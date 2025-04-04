# Generated by Django 4.2 on 2025-03-17 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0004_remove_song_duration"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="songs",
        ),
        migrations.AddField(
            model_name="post",
            name="net_votes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="song",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="songs.song",
            ),
        ),
    ]
