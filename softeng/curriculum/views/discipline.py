# from django.views.generic import ListView, DetailView
# from django.shortcuts import get_object_or_404
# from django.urls import reverse_lazy
# from django.contrib import messages
# from knowledge.models import Subtopic
# from core.generics import ObjectRedirectView
# from curriculum.models import Discipline


# class DisciplineListView(ListView):
#     """
#     Page to list all disciplines into their flux.
#     """

#     model = Discipline
#     template_name = "curriculum/disciplines.html"
#     context_object_name = "disciplines"

#     def get_context_data(self, **kwargs):
#         """
#         Get discipline to specific semestes.
#         """

#         context = super(DisciplineListView, self).get_context_data(**kwargs)

#         context['first_semester'] = Discipline.objects.filter(semester=1)
#         context['second_semester'] = Discipline.objects.filter(semester=2)
#         context['third_semester'] = Discipline.objects.filter(semester=3)
#         context['fourth_semester'] = Discipline.objects.filter(semester=4)
#         context['fifth_semester'] = Discipline.objects.filter(semester=5)
#         context['sixth_semester'] = Discipline.objects.filter(semester=6)
#         context['seventh_semester'] = Discipline.objects.filter(semester=7)
#         context['eighth_semester'] = Discipline.objects.filter(semester=8)
#         context['ninth_semester'] = Discipline.objects.filter(semester=9)
#         context['tenth_semester'] = Discipline.objects.filter(semester=10)

#         return context


# class DisciplineDetailView(DetailView):
#     """
#     View to show a specific discipline.
#     """

#     model = Discipline
#     template_name = "curriculum/details.html"
#     context_object_name = "discipline"


# class RemoveContentView(ObjectRedirectView):
#     """
#     Remove a content from discipline.
#     """

#     template_name = "curriculum/details.html"

#     def get_object(self):
#         """
#         Get the specific content.
#         """

#         discipline = get_object_or_404(
#             Discipline,
#             slug=self.kwargs.get('slug', '')
#         )

#         return discipline

#     def get_success_url(self):
#         """
#         Create a success url to redirect
#         """

#         discipline = self.get_object()

#         success_url = reverse_lazy(
#             'curriculum:discipline-detail',
#             kwargs={
#                 'slug': discipline.slug
#             }
#         )

#         return success_url

#     def action(self, request, *args, **kwargs):
#         """
#         Remove content from discipline.
#         """

#         discipline = self.get_object()

#         subtopic = get_object_or_404(
#             Subtopic,
#             slug=self.kwargs.get('subtopic', '')
#         )

#         discipline.program.remove(subtopic)

#         messages.success(
#             self.request,
#             "Subtopic removed successfully"
#         )

#         return super(RemoveContentView, self).action(request, *args, **kwargs)
