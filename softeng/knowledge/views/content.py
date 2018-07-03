from core.query import Query
from django.views.generic import ListView, DetailView
from core.generics import ObjectRedirectView
from django.urls import reverse_lazy
from django.contrib import messages
from curriculum.models import Disciplines
# from knowledge.models import Topics, Subtopics, Subtopic


# class InsertContentListView(ListView):
#     """
#     Page to insert specific content into a specific discipline.
#     """

#     template_name = "knowledge/insert_content.html"
#     context_object_name = "disciplines"
#     paginate_by = 20

#     def get_context_data(self, **kwargs):
#         """
#         Get the subtopic and list of disciplines.
#         """

#         context = super(InsertContentListView, self).get_context_data(**kwargs)
#         context['topic'] = self.get_topics()
#         context['subtopic'] = self.get_subtopics()
#         return context

#     def get_topic(self):
#         """
#         Get the specific topic.
#         """

#         topics = Topics().get_topics()

#         slug = self.kwargs.get('topic', '')

#         for topic in topics:
#             if topic.slug == slug:
#                 return topic

#         return None

#     def get_subtopic(self):
#         """
#         Get the specific subtopic.
#         """

#         subtopics = Topics().get_subtopics()

#         slug = self.kwargs.get('subtopic', '')

#         for subtopic in subtopics:
#             if subtopic.slug == slug:
#                 return subtopic

#         return None
