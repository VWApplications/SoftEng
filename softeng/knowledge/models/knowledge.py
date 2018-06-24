from django.db import models
from curriculum.models import CoreContent
from .swebok import Swebok


class Knowledge(Swebok):
    """
    Create Knowledge model.
    """

    core_content = models.ForeignKey(
        CoreContent,
        on_delete=models.SET_NULL,
        related_name="knowledges",
        null=True
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
