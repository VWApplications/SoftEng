from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from curriculum.models import CoreContent
from knowledge.models import Knowledge, Topic


class SwebokListView(ListView):
    """
    Page to list all core content of swebok.
    """

    model = CoreContent
    template_name = "knowledge/swebok.html"
    context_object_name = "swebok"


class SwebokDetailView(DetailView):
    """
    View to show a specific knowledge and their topics.
    """

    model = Knowledge
    template_name = "knowledge/swebok_details.html"
    context_object_name = "knowledge"


class TopicDetailView(DetailView):
    """
    View to show a specific topic and their subtopics.
    """

    template_name = "knowledge/topic_details.html"
    context_object_name = "topic"

    def get_object(self):
        """
        Get the specific topic.
        """

        topic = get_object_or_404(
            Topic,
            slug=self.kwargs.get('topic', '')
        )

        return topic
