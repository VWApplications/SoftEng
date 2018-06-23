from django.db import models
from django.core import validators
from knowledge.models import Subtopic


class Discipline(models.Model):
    """
    Create a discipline model.
    """

    title = models.CharField(
        'Title',
        max_length=100,
        help_text="Discipline title."
    )

    code = models.PositiveIntegerField(
        'Code',
        help_text="Discipline code."
    )

    institution = models.CharField(
        'Institution',
        max_length=100,
        help_text="Discipline institution",
        blank=True
    )

    SEMESTERS = (
        (1, 'First Semester'),
        (2, 'Second Semester'),
        (3, 'Third Semester'),
        (4, 'Fourth Semester'),
        (5, 'Fifth Semester'),
        (6, 'Sixth Semester'),
        (7, 'Seventh Semester'),
        (8, 'Eighth Semester'),
        (9, 'Ninth Semester'),
        (10, 'Tenth Semester'),
    )

    semester = models.PositiveIntegerField(
        'Semester',
        help_text="Discipline semester.",
        choices=SEMESTERS
    )

    TYPE = (
        ('Required', "Required"),
        ('Optional', "Optional")
    )

    classification = models.CharField(
        'Classification',
        max_length=8,
        help_text="Discipline classification.",
        choices=TYPE,
        default="Required"
    )

    description = models.TextField(
        'Description',
        help_text="Discipline description.",
        blank=True
    )

    credits = models.PositiveIntegerField(
        'Credits',
        help_text="Discipline credits",
        validators=[
            validators.MaxLengthValidator(10),
            validators.MinLengthValidator(1)
        ]
    )

    bibliografy = models.TextField(
        'Bibliografy',
        help_text="Bibliografy",
        blank=True
    )

    required = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="is_required_in",
        blank=True
    )

    program = models.ManyToManyField(
        Subtopic,
        related_name="disciplines",
        blank=True
    )

    slug = models.SlugField(
        'Shortcut',
        help_text="URL string shortcut"
    )

    created_at = models.DateTimeField(
        'Created at',
        help_text="Date that the discipline is created.",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated at',
        help_text="Date that the discipline is updated.",
        auto_now=True
    )

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent the
        objet
        """

        return "{0} - {1}".format(self.code, self.title)

    class Meta:
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"
        ordering = ['semester']
