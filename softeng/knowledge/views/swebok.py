from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from knowledge.models import Knowledge


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

    def get_context_data(self, **kwargs):
        """
        Get the subtopic and list of disciplines.
        """

        context = super(SwebokDetailView, self).get_context_data(**kwargs)
        context['knowledge'] = self.get_knowledge()
        return context

    def get_knowledges(self):
        """
        Get all knowledges.
        """

        knowledge = Knowledge()
        knowledges = knowledge.get_instance()

        return knowledges

    def get_knowledge(self):
        """
        Get the specific knowledge.
        """

        knowledges = self.get_knowledges()
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

        for topic in knowledge.get_topic():
            if topic_slug == topic.slug:
                return topic

        messages.error(
            self.request,
            "Topic not found"
        )

        redirect('knowledge:swebok-list')
