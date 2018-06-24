from django.db import migrations
from django.utils.text import slugify
from curriculum.models import (
    CourseCompletionWork, IntegratorProject,
    SupervisedInternship
)


def multidisciplinary_forwards(apps, schema_editor):
    """
    Create multidisciplinary instance into Multidisciplinary model.
    """

    Multidisciplinary = apps.get_model("curriculum", "Multidisciplinary")
    db_alias = schema_editor.connection.alias

    multidisciplinaries = []
    multidisciplinaries.append(CourseCompletionWork())
    multidisciplinaries.append(IntegratorProject())
    multidisciplinaries.append(SupervisedInternship())

    for multidisciplinary in multidisciplinaries:
        Multidisciplinary.objects.using(db_alias).bulk_create([
            Multidisciplinary(
                title=multidisciplinary.title,
                description=multidisciplinary.description,
                slug=slugify(multidisciplinary.title),
            )
        ])


def multidisciplinary_reverse(apps, schema_editor):
    """
    Remove all instances of multidisciplinary.
    """

    Multidisciplinary = apps.get_model("curriculum", "Multidisciplinary")
    db_alias = schema_editor.connection.alias
    Multidisciplinary.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_extension_fixture'),
    ]

    operations = [
        migrations.RunPython(multidisciplinary_forwards, multidisciplinary_reverse)
    ]
