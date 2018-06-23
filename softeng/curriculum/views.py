from django.views.generic import ListView, DetailView
from .models import Discipline


class DisciplineListView(ListView):
    """
    Page to list all disciplines into their flux.
    """

    template_name = "curriculum/disciplines.html"
    context_object_name = "disciplines"

    def get_context_data(self, **kwargs):
        """
        Get discipline to specific semestes.
        """

        context = super(DisciplineListView, self).get_context_data(**kwargs)

        context['first_semester'] = Discipline.objects.filter(semester=1)
        context['second_semester'] = Discipline.objects.filter(semester=2)
        context['third_semester'] = Discipline.objects.filter(semester=3)
        context['fourth_semester'] = Discipline.objects.filter(semester=4)
        context['fifth_semester'] = Discipline.objects.filter(semester=5)
        context['sixth_semester'] = Discipline.objects.filter(semester=6)
        context['seventh_semester'] = Discipline.objects.filter(semester=7)
        context['eighth_semester'] = Discipline.objects.filter(semester=8)
        context['ninth_semester'] = Discipline.objects.filter(semester=9)
        context['tenth_semester'] = Discipline.objects.filter(semester=10)

        return context

    def get_queryset(self):
        """
        Get the discipline queryset from model database.
        """

        queryset = Discipline.objects.all()

        return queryset


class DisciplineDetailView(DetailView):
    """
    View to show a specific discipline.
    """

    model = Discipline
    template_name = "curriculum/details.html"
