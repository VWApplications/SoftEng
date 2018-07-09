from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from knowledge.models import Knowledges


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

        knowledges = Knowledges.get_knowledges()

        return knowledges


class SwebokDetailView(DetailView):
    """
    View to show a specific topic and their subtopics.
    """

    template_name = "knowledge/swebok_details.html"
    context_object_name = "topic"
    slug_url_kwarg = "topic"

    def get_context_data(self, **kwargs):
        """
        Get the subtopic and list of disciplines.
        """

        context = super(SwebokDetailView, self).get_context_data(**kwargs)
        context['knowledge'] = self.get_knowledge()
        return context

    def get_knowledge(self):
        """
        Get the specific knowledge.
        """

        knowledges = Knowledges.get_knowledges()
        knowledge_slug = self.kwargs.get('knowledge', '')

        for knowledge in knowledges:
            if knowledge.slug == knowledge_slug:
                return knowledge

    def get_object(self):
        """
        Get the specific topic.
        """

        knowledge = self.get_knowledge()

        topic_slug = self.kwargs.get('topic', '')

        for topic in knowledge.topics:
            if topic_slug == topic.slug:
                return topic

        messages.error(
            self.request,
            "Topic not found"
        )

        redirect('knowledge:swebok-list')
