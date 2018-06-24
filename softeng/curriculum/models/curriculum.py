from django.db import models


class PedagogicalProject(models.Model):
    """
    Abstract class to Pedagogical project.
    """

    title = models.CharField(
        'Title',
        max_length=100,
        help_text="Core content title."
    )

    description = models.TextField(
        'Description',
        help_text="Core content description.",
        blank=True
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        help_text="Date that the core content is created.",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        help_text="Date that the core content is updated.",
        auto_now=True
    )

    class Meta:
        abstract = True


class CoreContent(PedagogicalProject):
    """
    Create Core Content model.
    """

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Core Content"
        verbose_name_plural = "Core Contents"
        ordering = ['title']


class Extension(PedagogicalProject):
    """
    Create Extension model.
    """

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Extension"
        verbose_name_plural = "Extensions"
        ordering = ['title']


class Multidisciplinary(PedagogicalProject):
    """
    Create Multidisciplinary model.
    """

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return self.title

    class Meta:
        verbose_name = "Multidisciplinary"
        verbose_name_plural = "Multidisciplinary"
        ordering = ['title']
