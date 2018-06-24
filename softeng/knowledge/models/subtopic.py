from django.db import models
from .topic import Topic
from .swebok import Swebok


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
