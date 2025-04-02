"""Django apps file that defines the configuration class for the Post app."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"

    def ready(self):
        import posts.signals  # noqa F401
