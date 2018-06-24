from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from core.generics import ObjectRedirectView
from knowledge.models import Topic, Subtopic
from curriculum.models import Discipline, CoreContent


class InsertContentListView(ListView):
    """
    Page to insert specific content into a specific discipline.
    """

    template_name = "knowledge/insert_content.html"
    context_object_name = "disciplines"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        """
        Get the subtopic and list of disciplines
        """

        context = super(InsertContentListView, self).get_context_data(**kwargs)
        context['topic'], context['subtopic'] = self.get_objects()
        return context

    def get_objects(self):
        """
        Get the specific content.
        """

        topic = get_object_or_404(
            Topic,
            slug=self.kwargs.get('topic', '')
        )

        subtopic = get_object_or_404(
            Subtopic,
            slug=self.kwargs.get('subtopic', '')
        )

        return topic, subtopic

    def get_queryset(self):
        """
        Get all disciplines.
        """

        queryset = Discipline.objects.all()

        topic, subtopic = self.get_objects()

        for discipline in queryset:
            if discipline in subtopic.disciplines.all():
                queryset = queryset.exclude(title=discipline.title)

        queryset = self.filter_disciplines(queryset)

        queryset = self.search_disciplines(queryset)

        return queryset

    def filter_disciplines(self, queryset):
        """
        Filter the discipline by...
        """

        core = self.request.GET.get('core')
        if core:
            if core == "basic":
                title = "Core Basic Content"
            elif core == "specific":
                title = "Core Specific Content"
            else:
                title = "Core Professional Content"

            try:
                core_content = CoreContent.objects.get(title=title)
                queryset = queryset.filter(core_content=core_content)
                print(core_content)
            except Exception:
                pass

        ordered = self.request.GET.get('order')
        if ordered:
            queryset = queryset.order_by(ordered)

        return queryset

    def search_disciplines(self, queryset):
        """
        Search the discipline by name or code.
        """

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset


class InsertContentView(ObjectRedirectView):
    """
    Insert specific content into a specific discipline.
    """

    template_name = "knowledge/insert_content.html"

    def get_object(self):
        """
        Get the specific discipline.
        """

        discipline = get_object_or_404(
            Discipline,
            slug=self.kwargs.get('discipline', '')
        )

        return discipline

    def get_subtopic(self):
        """
        Get the specific subtopic.
        """

        subtopic = get_object_or_404(
            Subtopic,
            slug=self.kwargs.get('subtopic', '')
        )

        return subtopic

    def get_success_url(self):
        """
        Create a success url to redirect
        """

        topic = get_object_or_404(
            Topic,
            slug=self.kwargs.get('topic', '')
        )

        subtopic = self.get_subtopic()

        success_url = reverse_lazy(
            'knowledge:disciplines',
            kwargs={
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

        success = True

        for discipline_subtopic in discipline.program.all():
            if discipline_subtopic == subtopic:
                success = False

        print(success)

        if success:
            discipline.program.add(subtopic)
            discipline.save()
            messages.success(
                self.request,
                "Subtopic inserted successfully"
            )
        else:
            messages.error(
                self.request,
                "Discipline content already exists"
            )

        return super(InsertContentView, self).action(request, *args, **kwargs)
