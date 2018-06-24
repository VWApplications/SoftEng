from django.db import models


class Swebok(models.Model):
    """
    Create Swebok abstract model.
    """

    title = models.CharField(
        'Title',
        max_length=100
    )

    description = models.TextField(
        'Description',
        blank=True
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        auto_now=True
    )

    class Meta:
        abstract = True
