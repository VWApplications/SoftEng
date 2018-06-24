from django.views.generic import ListView, DetailView
from curriculum.models import CoreContent
from knowledge.models import Knowledge


class SwebokListView(ListView):
    """
    Page to list all core content of swebok.
    """

    model = CoreContent
    template_name = "knowledge/swebok.html"
    context_object_name = "swebok"


class SwebokDetailView(DetailView):
    """
    View to show a specific core content.
    """

    model = Knowledge
    template_name = "knowledge/swebok_details.html"
    context_object_name = "knowledge"
