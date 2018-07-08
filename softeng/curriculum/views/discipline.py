from core.query import Query
from django.template.defaultfilters import slugify
from django.views.generic import (
    ListView, DetailView, FormView
)
from core.generics import ObjectRedirectView
from core.utils import create_uri
from django.urls import reverse_lazy
from django.contrib import messages
from curriculum.models import Disciplines
from curriculum.forms import DisciplineForm


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


class DisciplineCreateView(FormView):
    """
    Create a new discipline.
    """

    template_name = "curriculum/form.html"
    form_class = DisciplineForm
    success_url = reverse_lazy('curriculum:discipline-list')

    def discipline_exists(self, title):
        """
        Verify if exists the discipline into triple store
        """

        disciplines = Disciplines()

        for discipline in disciplines.all:
            if discipline.slug == slugify(title):
                return True

        return False

    def form_valid(self, form):
        """
        Receive the form already validated to create a discipline.
        """

        title = form.cleaned_data['title']
        uri = create_uri(title)
        code = form.cleaned_data['code']
        description = form.cleaned_data['description']
        classification = create_uri(form.cleaned_data['classification'])
        flow = create_uri(form.cleaned_data['flow'])
        core = create_uri(form.cleaned_data['core'])

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            INSERT {
                pp:%s rdfs:subClassOf pp:Discipline ;
                pp:belongsTo pp:Software_Engineering ;
                pp:hasType pp:%s ;
                pp:isInTheFlowOf pp:%s ;
                pp:isPartOf pp:%s ;
                dc:title "%s" ;
                pp:code "%s" ;
                dc:description "%s"
            } WHERE {}
        """ % (
            uri, classification, flow, core,
            title, code, description
        )

        if self.discipline_exists(title):
            messages.success(
                self.request,
                "This discipline already exists"
            )
        else:
            response = Query.update(query)

            if response == 204:
                messages.success(
                    self.request,
                    "Discipline created successfully"
                )
            else:
                messages.success(
                    self.request,
                    "There was a server error"
                )

        return super(DisciplineCreateView, self).form_valid(form)


class DisciplineRemoveView(ObjectRedirectView):
    """
    Remove a specific discipline
    """

    template_name = "curriculum/details.html"

    def get_object(self):
        """
        Get the specific discipline.
        """

        disciplines = Disciplines().get_disciplines("rdfs:subClassOf", "pp:Discipline")

        slug = self.kwargs.get('discipline', '')

        for discipline in disciplines:
            if discipline.slug == slug:
                return discipline

        return None

    def get_success_url(self):
        """
        Get success url.
        """

        success_url = reverse_lazy('curriculum:discipline-list')

        return success_url

    def remove_subtopics(self):
        """
        Remove all subtopics from discipline.
        """
        discipline = self.get_object()

        subtopics = Disciplines.get_contents(discipline.uri)

        if subtopics:
            for subtopic in subtopics:
                query = """
                    PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
                    DELETE {<%s> pp:hasContent <%s>} WHERE {}
                """ % (discipline.uri, subtopic.uri)

                Query.update(query)

    def action(self, request, *args, **kwargs):
        """
        Remove the discipline triples from triple store.
        """

        discipline = self.get_object()

        self.remove_subtopics()

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            DELETE {
                <%s> rdfs:subClassOf pp:Discipline ;
                pp:belongsTo pp:Software_Engineering ;
                pp:hasType pp:%s ;
                pp:isInTheFlowOf pp:%s ;
                pp:isPartOf pp:%s ;
                dc:title "%s" ;
                pp:code "%s" ;
                dc:description "%s"
            } WHERE {}
        """ % (
            discipline.uri,
            create_uri(discipline.classification),
            create_uri(discipline.semester),
            create_uri(discipline.core_content),
            discipline.title,
            discipline.code,
            discipline.description
        )

        response = Query.update(query)

        if response == 204:
            messages.success(
                self.request,
                "Discipline removed successfully"
            )
        else:
            messages.success(
                self.request,
                "There was a server error"
            )

        return super(DisciplineRemoveView, self).action(request, *args, **kwargs)


class DisciplineUpdateView(FormView):
    """
    Update a specific discipline.
    """

    template_name = "curriculum/form.html"
    form_class = DisciplineForm
    success_url = reverse_lazy('curriculum:discipline-list')

    def get_object(self):
        """
        Get the specific discipline.
        """

        disciplines = Disciplines().get_disciplines("rdfs:subClassOf", "pp:Discipline")

        slug = self.kwargs.get('discipline', '')

        for discipline in disciplines:
            if discipline.slug == slug:
                return discipline

        return None

    def get_context_data(self, **kwargs):
        """
        Get discipline to specific semestes.
        """

        context = super(DisciplineUpdateView, self).get_context_data(**kwargs)

        context['discipline'] = self.get_object()

        return context

    def remove_discipline(self):
        """
        Remove the discipline triples from triple store.
        """

        discipline = self.get_object()

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            DELETE {
                <%s> rdfs:subClassOf pp:Discipline ;
                pp:belongsTo pp:Software_Engineering ;
                pp:hasType pp:%s ;
                pp:isInTheFlowOf pp:%s ;
                pp:isPartOf pp:%s ;
                dc:title "%s" ;
                pp:code "%s" ;
                dc:description "%s"
            } WHERE {}
        """ % (
            discipline.uri,
            create_uri(discipline.classification),
            create_uri(discipline.semester),
            create_uri(discipline.core_content),
            discipline.title,
            discipline.code,
            discipline.description
        )

        response = Query.update(query)

        return response

    def form_valid(self, form):
        """
        Receive the form already validated to create a discipline.
        """

        response = self.remove_discipline()

        title = form.cleaned_data['title']
        uri = create_uri(title)
        code = form.cleaned_data['code']
        description = form.cleaned_data['description']
        classification = create_uri(form.cleaned_data['classification'])
        flow = create_uri(form.cleaned_data['flow'])
        core = create_uri(form.cleaned_data['core'])

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            INSERT {
                pp:%s rdfs:subClassOf pp:Discipline ;
                pp:belongsTo pp:Software_Engineering ;
                pp:hasType pp:%s ;
                pp:isInTheFlowOf pp:%s ;
                pp:isPartOf pp:%s ;
                dc:title "%s" ;
                pp:code "%s" ;
                dc:description "%s"
            } WHERE {}
        """ % (
            uri, classification, flow, core,
            title, code, description
        )

        if response == 204:
            response = Query.update(query)

        if response == 204:
            messages.success(
                self.request,
                "Discipline updated successfully"
            )
        else:
            messages.success(
                self.request,
                "There was a server error"
            )

        return super(DisciplineUpdateView, self).form_valid(form)


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
