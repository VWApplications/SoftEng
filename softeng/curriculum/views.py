from django.views.generic import ListView
from .models import Discipline


class DisciplineListView(ListView):
    """
    Page to list all disciplines into their flux.
    """

    template_name = "curriculum/disciplines.html"
    context_object_name = "disciplines"

    def get_queryset(self):
        """
        Get the discipline queryset from model database.
        """

        queryset = Discipline.objects.all()

        return queryset
