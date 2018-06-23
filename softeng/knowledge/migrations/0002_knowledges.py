from django.db import migrations
from knowledge.models import ComputingFoundations


def knowledges_forwards(apps, schema_editor):
    """
    Create Knowledges instance into Knowledge model.
    """

    Knowledge = apps.get_model("knowledge", "Knowledge")
    db_alias = schema_editor.connection.alias

    knowledges = []
    knowledges.append(ComputingFoundations())

    for knowledge in knowledges:
        Knowledge.objects.using(db_alias).bulk_create([
            Knowledge(
                title=knowledge.title,
                description=knowledge.description,
                slug=knowledge.title,
            )
        ])


def knowledges_reverse(apps, schema_editor):
    """
    Remove all instances of Knowledge.
    """

    Knowledge = apps.get_model("knowledge", "Knowledge")
    db_alias = schema_editor.connection.alias
    Knowledge.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(knowledges_forwards, knowledges_reverse)
    ]
