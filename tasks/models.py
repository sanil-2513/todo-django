from django.db import models


class Task(models.Model):
    """Represent a single todo task."""

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the task title as its string representation."""
        return self.title