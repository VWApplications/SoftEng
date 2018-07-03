from core.query import Query
from django.views.generic import ListView, DetailView
from core.generics import ObjectRedirectView
from django.urls import reverse_lazy
from django.contrib import messages
from curriculum.models import Disciplines


class DisciplineListView(ListView):
    """
    Page to list all disciplines into their flux.
    """

    template_name = "curriculum/disciplines.html"
    context_object_name = "disciplines"

    def get_queryset(self):
        """
        Get all disciplines.
        """

        disciplines = Disciplines()

        return disciplines.all

    def get_context_data(self, **kwargs):
        """
        Get discipline to specific semestes.
        """

        disciplines = Disciplines()

        context = super(DisciplineListView, self).get_context_data(**kwargs)

        context['first_semester'] = disciplines.first_semester
        context['second_semester'] = disciplines.second_semester
        context['third_semester'] = disciplines.third_semester
        context['fourth_semester'] = disciplines.fourth_semester
        context['fifth_semester'] = disciplines.fifth_semester
        context['sixth_semester'] = disciplines.sixth_semester
        context['seventh_semester'] = disciplines.seventh_semester
        context['eighth_semester'] = disciplines.eighth_semester
        context['ninth_semester'] = disciplines.ninth_semester
        context['tenth_semester'] = disciplines.tenth_semester

        return context


class DisciplineDetailView(DetailView):
    """
    View to show a specific discipline.
    """

    template_name = "curriculum/details.html"
    context_object_name = "discipline"

    def get_object(self):
        """
        Get the specific discipline.
        """

        disciplines = Disciplines().get_disciplines("rdfs:subClassOf", "pp:Discipline")

        slug = self.kwargs.get('slug', '')

        for discipline in disciplines:
            if discipline.slug == slug:
                return discipline

        return None

    def get_context_data(self, **kwargs):
        """
        Get discipline to specific semestes.
        """

        context = super(DisciplineDetailView, self).get_context_data(**kwargs)

        discipline = self.get_object()

        context['are_requireds_of'] = Disciplines.get_is_required_of(discipline.uri)

        context['requireds'] = Disciplines.get_requireds(discipline.uri)

        context['program'] = Disciplines.get_contents(discipline.uri)

        return context


class RemoveContentView(ObjectRedirectView):
    """
    Remove a content from discipline.
    """

    template_name = "curriculum/details.html"

    def get_object(self):
        """
        Get the specific discipline
        """

        disciplines = Disciplines().get_disciplines("rdfs:subClassOf", "pp:Discipline")

        slug = self.kwargs.get('slug', '')

        for discipline in disciplines:
            if discipline.slug == slug:
                return discipline

        return None

    def get_subtopic(self):
        """
        Get the specific subtopic of discipline.
        """

        discipline = self.get_object()

        subtopics = Disciplines.get_contents(discipline.uri)

        slug = self.kwargs.get('subtopic', '')

        for subtopic in subtopics:
            if subtopic.slug == slug:
                return subtopic

        return None

    def get_success_url(self):
        """
        Get success url.
        """

        discipline = self.get_object()

        success_url = reverse_lazy(
            'curriculum:discipline-detail',
            kwargs={'slug': discipline.slug}
        )

        return success_url

    def action(self, request, *args, **kwargs):
        """
        Remove the triple from triple store.
        """

        discipline = self.get_object()
        subtopic = self.get_subtopic()

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            DELETE {<%s> pp:hasContent <%s>} WHERE {}
        """ % (discipline.uri, subtopic.uri)

        response = Query.update(query)

        if response == 204:
            messages.success(
                self.request,
                "Subtopic removed successfully"
            )
        else:
            messages.success(
                self.request,
                "There was a server error"
            )

        return super(RemoveContentView, self).action(request, *args, **kwargs)
