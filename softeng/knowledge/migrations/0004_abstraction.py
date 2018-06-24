from django.db import migrations
from django.utils.text import slugify
from knowledge.models import ComputingFoundations


def get_topic(apps, title):
    """
    Get abstraction topic
    """

    Topic = apps.get_model('knowledge', 'Topic')

    try:
        topic = Topic.objects.get(title=title)
    except Exception:
        topic = None

    return topic


def abstraction_forwards(apps, schema_editor):
    """
    Create abstraction subtopics instance into Subtopic model.
    """

    Subtopic = apps.get_model("knowledge", "Subtopic")
    knowledge = ComputingFoundations()
    topic = knowledge.get_topic(knowledge.ABSTRACTION)

    subtopics = []
    subtopics.append(topic.get_subtopic(topic.ALTERNATE_ABSTRACTIONS))
    subtopics.append(topic.get_subtopic(topic.ENCAPSULATION))
    subtopics.append(topic.get_subtopic(topic.HIERARCHY))
    subtopics.append(topic.get_subtopic(topic.LEVELS_OF_ABSTRACTION))

    for subtopic in subtopics:
        Subtopic.objects.create(
            title=subtopic.title,
            description=subtopic.description,
            topic=get_topic(apps, topic.title),
            slug=slugify(subtopic.title),
        )


def abstraction_reverse(apps, schema_editor):
    """
    Remove all instances of abstraction subtopics.
    """

    Subtopic = apps.get_model("knowledge", "Subtopic")
    Subtopic.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0003_computing_foundations'),
    ]

    operations = [
        migrations.RunPython(abstraction_forwards, abstraction_reverse)
    ]
