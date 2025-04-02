"""Django models file that defines the ORM model for the Song entity."""

from django.db import models
import cloudinary

from base_content.models import BaseContent


class Song(BaseContent):
    """Defines a single Song with a short audio file linked by a URL.
    Inherits from BaseContent, a class that defines fields shared between Song
    and Post.

    Fields:
    audio_file: models.FileField -- a field to temporarily save the audio file
                                    for a new song whilst the cloudinary upload
                                    is processing. No utility for the frontend
                                    after the initial Song creation.
    audio_url: models.URLField -- the URL to the cloudinary hosted song clip; how
                                  the Song's audio should be accessed by the frontend.
    artist_name: models.CharField -- the name of the artist responsible for this Song.
                                     Defined independently of the User's username as the
                                     'artist' name and username may be different.
    link_to_song: models.URLField -- optionally, a URL to the full song, since only short
                                     clips of audio are to be saved with the Song model.

    Methods:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its id, title and artist name.
    save -- custom save method to overwrite the standard django Model save functionality.
            Uploads the audio file to cloudinary and saves the secure URL to the audio_url field.
    """

    audio_file = models.FileField(upload_to="temp_audio/", blank=True, null=True)
    audio_url = models.URLField(blank=True, max_length=500)
    artist_name = models.CharField(max_length=255)
    link_to_song = models.URLField(blank=True, max_length=200)

    def __str__(self):
        """Return a string to represent the Song model."""
        return f"{self.id}: {self.title} by {self.artist_name}"

    def save(self, *args, **kwargs):
        """Overwrite the default save functionality so the audio_file given can be
        uploaded to Cloudinary and accessed via the audio_url field.
        """
        if self.audio_file and not self.audio_url:
            # Upload file directly to Cloudinary using the file-like object
            result = cloudinary.uploader.upload(
                self.audio_file,
                resource_type="raw",  # Specify raw resource type for non-image files
                folder="audio_files/",  # Save in a specific folder on Cloudinary
            )
            self.audio_url = result["secure_url"]  # Save the Cloudinary HTTPS URL

            # Clean up the file after upload
            self.audio_file.delete(save=False)

        super().save(*args, **kwargs)  # Call the parent class's save method
