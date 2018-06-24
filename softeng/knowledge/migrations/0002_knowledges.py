from django.db import migrations
from django.utils.text import slugify
from knowledge.models import ComputingFoundations


def knowledges_forwards(apps, schema_editor):
    """
    Create Knowledges instance into Knowledge model.
    """

    Knowledge = apps.get_model("knowledge", "Knowledge")

    knowledges = []
    knowledges.append(ComputingFoundations())

    for knowledge in knowledges:
        Knowledge.objects.create(
            title=knowledge.title,
            description=knowledge.description,
            slug=slugify(knowledge.title),
        )


def knowledges_reverse(apps, schema_editor):
    """
    Remove all instances of Knowledge.
    """

    Knowledge = apps.get_model("knowledge", "Knowledge")
    Knowledge.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(knowledges_forwards, knowledges_reverse)
    ]
