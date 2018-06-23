from django.db import models


class Knowledge(models.Model):
    """
    Create Knowledge model.
    """

    title = models.CharField(
        'Title',
        max_length=100,
        help_text="Knowledge title."
    )

    description = models.TextField(
        'Description',
        help_text="Knowledge description.",
        blank=True
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        help_text="Date that the knowledge is created.",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        help_text="Date that the knowledge is updated.",
        auto_now=True
    )

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Knowledge"
        verbose_name_plural = "Knowledges"
        ordering = ['title']
