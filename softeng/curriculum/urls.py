from django.urls import path
from .views import discipline, curriculum

app_name = 'curriculum'

urlpatterns = [
    # disciplines/
    path(
        "disciplines/",
        discipline.DisciplineListView.as_view(),
        name='discipline-list'
    ),
    # disciplines/create/
    path(
        "disciplines/create/",
        discipline.DisciplineCreateView.as_view(),
        name='discipline-create'
    ),
    # disciplines/<slug>/details/
    path(
        "disciplines/<slug:slug>/details/",
        discipline.DisciplineDetailView.as_view(),
        name="discipline-detail"
    ),
    # disciplines/<slug>/remove/
    path(
        "disciplines/<slug:discipline>/remove/",
        discipline.DisciplineRemoveView.as_view(),
        name="discipline-remove"
    ),
    # disciplines/<slug>/<subtopic>/details/
    path(
        "disciplines/<slug:slug>/<slug:subtopic>/remove/",
        discipline.RemoveContentView.as_view(),
        name="remove"
    ),
    # extensions/
    path(
        "extensions/",
        curriculum.ExtensionListView.as_view(),
        name='extension-list'
    ),
    # core_contents/
    path(
        "core_contents/",
        curriculum.CoreContentListView.as_view(),
        name="core-content-list"
    ),
]
