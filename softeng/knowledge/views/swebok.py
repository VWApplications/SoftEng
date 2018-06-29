from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from knowledge.models import Knowledge
from knowledge.models.computing_foundations import ComputingFoundations


class SwebokListView(ListView):
    """
    Page to list all core content of swebok.
    """

    template_name = "knowledge/swebok.html"
    context_object_name = "swebok"

    def get_queryset(self):
        """
        Get all knowledges
        """

        knowledge = Knowledge()
        knowledges = knowledge.get_instance()

        return knowledges


class SwebokDetailView(DetailView):
    """
    View to show a specific topic and their subtopics.
    """

    template_name = "knowledge/swebok_details.html"
    context_object_name = "topic"
    slug_url_kwarg = "topic"

    def get_object(self):
        """
        Get the specific topic.
        """

        computing_foundations = ComputingFoundations()

        topic_slug = self.kwargs.get('topic', '')
        print(topic_slug)

        for topic in computing_foundations.get_topic():
            if topic_slug == topic.slug:
                return topic

        messages.error(
            self.request,
            "Topic not found"
        )

        redirect('knowledge:swebok-list')
