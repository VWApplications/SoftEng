from django.views.generic import ListView, DetailView
from knowledge.models import Knowledge, Topic


class SwebokListView(ListView):
    """
    Page to list all core content of swebok.
    """

    model = Knowledge
    template_name = "knowledge/swebok.html"
    context_object_name = "swebok"


class SwebokDetailView(DetailView):
    """
    View to show a specific topic and their subtopics.
    """

    model = Topic
    template_name = "knowledge/swebok_details.html"
    context_object_name = "topic"
    slug_url_kwarg = "topic"
