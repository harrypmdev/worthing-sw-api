"""Django models file that defines an abstract class, BaseContent,
from which Post and Song models inherit.
."""

from django.db import models
from django.contrib.auth.models import User


class BaseContent(models.Model):
    """Defines the BaseContent class, an abstract model class which defines
    fields shared by both the Song and Post model.

    Fields:
    user: models.ForeignKey -- the foreign key that links of BaseContent children
                               to a single User instance.
    title: models.CharField -- the title of the BaseContent item.
    created_at: models.DateTimeField -- the date and time of creation.
    updated_at: models.DateTimeField -- the date and time of the last update.
    net_votes: models.IntegerField -- the net votes for this BaseContent item.

    Method:
    __str__ -- python dunder method to define a string representation of the class.
               Summarises the class by its id and title.

    A django model Meta class defines the class as abstract and default ordering.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    net_votes = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id}: {self.title}"
