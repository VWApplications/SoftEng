from django.db import models
from .topic import Topic


class Subtopic(models.Model):
    """
    Create Subtopic model.
    """

    title = models.CharField(
        'Title',
        max_length=100,
        help_text="Subtopic title."
    )

    description = models.TextField(
        'Description',
        help_text="Subtopic description.",
        blank=True
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="subtopics"
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        help_text="Date that the subtopic is created.",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        help_text="Date that the subtopic is updated.",
        auto_now=True
    )

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Subtopic"
        verbose_name_plural = "Subtopics"
        ordering = ['title']
