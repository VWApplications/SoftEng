from core.query import Query
from django.views.generic import ListView
from core.generics import ObjectRedirectView
from django.urls import reverse_lazy
from django.contrib import messages
from curriculum.models import Disciplines
from knowledge.models import Knowledge


class InsertContentListView(ListView):
    """
    Page to insert specific content into a specific discipline.
    """

    template_name = "knowledge/insert_content.html"
    context_object_name = "disciplines"
    paginate_by = 20

    def get_queryset(self):
        """
        Get all disciplines
        """

        discipline = Disciplines()
        disciplines = discipline.get_disciplines('rdfs:subClassOf', 'pp:Discipline')

        return disciplines

    def get_context_data(self, **kwargs):
        """
        Get the subtopic and list of disciplines.
        """

        context = super(InsertContentListView, self).get_context_data(**kwargs)
        context['knowledge'] = self.get_knowledge()
        context['topic'] = self.get_topic()
        context['subtopic'] = self.get_subtopic()
        return context

    def get_knowledge(self):
        """
        Get the specific knowledge.
        """

        knowledge = Knowledge()
        knowledges = knowledge.get_instance()

        knowledge_slug = self.kwargs.get('knowledge', '')

        for knowledge in knowledges:
            if knowledge.slug == knowledge_slug:
                return knowledge

        return None

    def get_topic(self):
        """
        Get specific topic of knowledge.
        """

        knowledge = self.get_knowledge()

        topic_slug = self.kwargs.get('topic', '')

        for topic in knowledge.get_topic():
            if topic_slug == topic.slug:
                return topic

        return None

    def get_subtopic(self):
        """
        Get the specific subtopic.
        """

        topic = self.get_topic()
        subtopic_slug = self.kwargs.get('subtopic', '')

        for subtopic in topic.get_subtopic():
            if subtopic.slug == subtopic_slug:
                return subtopic

        return None


class InsertContentView(ObjectRedirectView):
    """
    Insert specific content into a specific discipline.
    """

    template_name = "knowledge/insert_content.html"

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

    def get_knowledge(self):
        """
        Get the specific knowledge.
        """

        knowledge = Knowledge()
        knowledges = knowledge.get_instance()

        knowledge_slug = self.kwargs.get('knowledge', '')

        for knowledge in knowledges:
            if knowledge.slug == knowledge_slug:
                return knowledge

        return None

    def get_topic(self):
        """
        Get specific topic of knowledge.
        """

        knowledge = self.get_knowledge()

        topic_slug = self.kwargs.get('topic', '')

        for topic in knowledge.get_topic():
            if topic_slug == topic.slug:
                return topic

        return None

    def get_subtopic(self):
        """
        Get the specific subtopic.
        """

        topic = self.get_topic()
        subtopic_slug = self.kwargs.get('subtopic', '')

        for subtopic in topic.get_subtopic():
            if subtopic.slug == subtopic_slug:
                return subtopic

        return None

    def get_success_url(self):
        """
        Create a success url to redirect.
        """

        knowledge = self.get_knowledge()
        topic = self.get_topic()
        subtopic = self.get_subtopic()

        success_url = reverse_lazy(
            'knowledge:disciplines',
            kwargs={
                'knowledge': knowledge.slug,
                'topic': topic.slug,
                'subtopic': subtopic.slug
            }
        )

        return success_url

    def action(self, request, *args, **kwargs):
        """
        Insert content into discipline.
        """

        discipline = self.get_object()
        subtopic = self.get_subtopic()

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            INSERT {<%s> pp:hasContent <%s>} WHERE {}
        """ % (discipline.uri, subtopic.uri)

        response = Query.update(query)

        if response == 204:
            messages.success(
                self.request,
                "Subtopic inserted successfully"
            )
        else:
            messages.success(
                self.request,
                "There was a server error"
            )

        return super(InsertContentView, self).action(request, *args, **kwargs)
