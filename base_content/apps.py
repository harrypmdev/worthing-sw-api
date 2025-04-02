"""Django apps file that defines the configuration class for the base_content app."""

from django.apps import AppConfig


class BaseContentConfig(AppConfig):
    """Configuration class for the base_content app.

    Fields:
    default_auto_field: string -- the default type for auto-generated primary keys.
    name: string -- the name of the app, as per the directory name.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "base_content"
