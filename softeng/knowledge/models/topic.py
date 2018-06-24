from django.db import models
from .knowledge import Knowledge
from .swebok import Swebok


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
