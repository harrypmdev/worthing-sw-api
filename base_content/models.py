from django.db import models
from django.contrib.auth.models import User


class BaseContent(models.Model):
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
