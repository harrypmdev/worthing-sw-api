# Generated by Django 4.2 on 2025-03-15 23:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0003_song_audio_url_alter_song_audio_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="duration",
        ),
    ]
