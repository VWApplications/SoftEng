from django.db import migrations
from django.utils.text import slugify
from curriculum.models import (
    ActivitiesOfSocialAction, ActivitiesOfStudentRepresentations,
    ExtensionActivities, MobilityAndExchangeActivities,
    ProfessionalPracticeActivities,
    ResearchActivities, TeachingActivities
)


def extension_forwards(apps, schema_editor):
    """
    Create extension instance into Extension model.
    """

    Extension = apps.get_model("curriculum", "Extension")
    db_alias = schema_editor.connection.alias

    extensions = []
    extensions.append(ActivitiesOfSocialAction())
    extensions.append(ActivitiesOfStudentRepresentations())
    extensions.append(ExtensionActivities())
    extensions.append(MobilityAndExchangeActivities())
    extensions.append(ProfessionalPracticeActivities())
    extensions.append(ResearchActivities())
    extensions.append(TeachingActivities())

    for extension in extensions:
        Extension.objects.using(db_alias).bulk_create([
            Extension(
                title=extension.title,
                description=extension.description,
                slug=slugify(extension.title),
            )
        ])


def extension_reverse(apps, schema_editor):
    """
    Remove all instances of extension.
    """

    Extension = apps.get_model("curriculum", "Extension")
    db_alias = schema_editor.connection.alias
    Extension.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_core_contents_fixture'),
    ]

    operations = [
        migrations.RunPython(extension_forwards, extension_reverse)
    ]
