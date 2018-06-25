from django.db import migrations
from django.utils.text import slugify
from curriculum.models import (
    CoreBasicContent, CoreSpecificContent,
    CoreProfessionalContent, FreeModule
)


def core_content_forwards(apps, schema_editor):
    """
    Create Core Content instance into CoreContent model.
    """

    CoreContent = apps.get_model("curriculum", "CoreContent")

    core_contents = []
    core_contents.append(CoreBasicContent())
    core_contents.append(CoreProfessionalContent())
    core_contents.append(CoreSpecificContent())
    core_contents.append(FreeModule())

    for core in core_contents:
        CoreContent.objects.create(
            title=core.title,
            description=core.description,
            slug=slugify(core.title),
        )


def core_content_reverse(apps, schema_editor):
    """
    Remove all instances of core content.
    """

    CoreContent = apps.get_model("curriculum", "CoreContent")
    CoreContent.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(core_content_forwards, core_content_reverse)
    ]
