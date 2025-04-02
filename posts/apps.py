"""Django apps file that defines the configuration class for the posts app."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Configuration class for the posts app.

    Fields:
    default_auto_field: string -- the default type for auto-generated primary keys.
    name: string -- the name of the app, as per the directory name.

    Methods:
    ready -- called when the application is fully loaded. Imports signals.py to
             ensure the signal receivers are recognised.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"

    def ready(self):
        """Import the signals file so Django recognises its functionality."""
        import posts.signals  # noqa F401
