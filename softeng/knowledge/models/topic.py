from django.db import models
from .knowledge import Knowledge


class Topic(models.Model):
    """
    Create Topic model.
    """

    title = models.CharField(
        'Title',
        max_length=100,
        help_text="Topic title."
    )

    description = models.TextField(
        'Description',
        help_text="Topic description.",
        blank=True
    )

    knowledge = models.ForeignKey(
        Knowledge,
        on_delete=models.CASCADE,
        related_name="topics"
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        help_text="Date that the topic is created.",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        help_text="Date that the topic is updated.",
        auto_now=True
    )

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ['title']
