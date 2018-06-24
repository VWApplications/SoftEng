from django.views.generic import ListView, DetailView
from curriculum.models import CoreContent
from knowledge.models import Knowledge


class SwebokListView(ListView):
    """
    Page to list all core content of swebok.
    """

    template_name = "knowledge/swebok.html"
    context_object_name = "swebok"

    def get_queryset(self):
        """
        Get the discipline queryset from model database.
        """

        queryset = CoreContent.objects.all()

        return queryset


class SwebokDetailView(DetailView):
    """
    View to show a specific core content.
    """

    model = Knowledge
    template_name = "knowledge/swebok_details.html"
    context_object_name = "knowledge"
