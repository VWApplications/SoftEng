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


class Knowledge(Swebok):
    """
    Create Knowledge model.
    """

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


class Topic(Swebok):
    """
    Create Topic model.
    """

    knowledge = models.ForeignKey(
        Knowledge,
        on_delete=models.CASCADE,
        related_name="topics"
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


class Subtopic(Swebok):
    """
    Create Subtopic model.
    """

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="subtopics"
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
