"""Django apps file that defines the configuration class for the songs app."""

from django.apps import AppConfig


class SongsConfig(AppConfig):
    """Configuration class for the songs app.

    Fields:
    default_auto_field: string -- the default type for auto-generated primary keys.
    name: string -- the name of the app, as per the directory name.

    Methods:
    ready -- called when the application is fully loaded. Imports signals.py to
             ensure the signal receivers are recognised.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "songs"

    def ready(self):
        """Import the signals file so Django recognises its functionality."""
        import songs.signals  # noqa F401
