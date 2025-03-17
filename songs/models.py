from django.db import models
import cloudinary

from base_content.models import BaseContent


class Song(BaseContent):
    audio_file = models.FileField(upload_to='temp_audio/', blank=True, null=True)
    audio_url = models.URLField(blank=True, max_length=500)
    artist_name = models.CharField(max_length=255)
    link_to_song = models.URLField(blank=True, max_length=200)
    net_votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.title} by {self.artist_name}'

    def save(self, *args, **kwargs):
        if self.audio_file and not self.audio_url:
            # Upload file directly to Cloudinary using the file-like object
            result = cloudinary.uploader.upload(
                self.audio_file,
                resource_type='raw',  # Specify raw resource type for non-image files
                folder='audio_files/'  # Save in a specific folder on Cloudinary
            )
            self.audio_url = result['url']  # Save the Cloudinary URL

            # Clean up the file after upload
            self.audio_file.delete(save=False)

        super().save(*args, **kwargs)  # Call the parent class's save method
