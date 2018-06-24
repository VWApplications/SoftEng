from django.db import migrations
from django.utils.text import slugify
from knowledge.models import ComputingFoundations


def get_knowledge(apps, title):
    """
    Get Computing Foundations knowledges
    """

    Knowledge = apps.get_model('knowledge', 'Knowledge')

    try:
        knowledge = Knowledge.objects.get(title=title)
    except Exception:
        knowledge = None

    return knowledge


def computing_foundations_forwards(apps, schema_editor):
    """
    Create Computing Foundations topics instance into Topic model.
    """

    Topic = apps.get_model("knowledge", "Topic")
    knowledge = ComputingFoundations()

    topics = []
    topics.append(knowledge.get_topic(knowledge.ABSTRACTION))
    topics.append(knowledge.get_topic(knowledge.ALGORITHMS_AND_COMPLEXITY))
    topics.append(knowledge.get_topic(knowledge.BASIC_CONCEPT_OF_A_SYSTEM))
    topics.append(knowledge.get_topic(knowledge.BASIC_DEVELOPER_HUMAN_FACTORS))
    topics.append(knowledge.get_topic(knowledge.BASIC_USER_HUMAN_FACTORS))
    # topics.append(knowledge.get_topic(knowledge.COMPILER_BASICS))
    # topics.append(knowledge.get_topic(knowledge.COMPUTER_ORGANIZATION))
    # topics.append(knowledge.get_topic(knowledge.DATA_STRUCTURE_AND_REPRESENTATION))
    # topics.append(knowledge.get_topic(knowledge.DATABASE_BASICS_AND_DATA_MANAGEMENT))
    # topics.append(knowledge.get_topic(knowledge.DEBUGGING_TOOLS_AND_TECHNIQUES))
    # topics.append(knowledge.get_topic(knowledge.NETWORK_COMMUNICATION_BASICS))
    # topics.append(knowledge.get_topic(knowledge.OPERATING_SYSTEMS_BASICS))
    # topics.append(knowledge.get_topic(knowledge.PARALLEL_AND_DISTRIBUTED_COMPUTING))
    topics.append(knowledge.get_topic(knowledge.PROBLEM_SOLVING_TECHNIQUES))
    topics.append(knowledge.get_topic(knowledge.PROGRAMMING_FUNDAMENTALS))
    # topics.append(knowledge.get_topic(knowledge.PROGRAMMING_LANGUAGE_BASICS))
    # topics.append(knowledge.get_topic(knowledge.SECURE_SOFTWARE_DEVELOPMENT_AND_MAINTENANCE))

    for topic in topics:
        Topic.objects.create(
            title=topic.title,
            description=topic.description,
            knowledge=get_knowledge(apps, knowledge.title),
            slug=slugify(topic.title),
        )


def computing_foundations_reverse(apps, schema_editor):
    """
    Remove all instances of Computing Foundations topics.
    """

    Topic = apps.get_model("knowledge", "Topic")
    Topic.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_knowledges'),
    ]

    operations = [
        migrations.RunPython(computing_foundations_forwards, computing_foundations_reverse)
    ]
