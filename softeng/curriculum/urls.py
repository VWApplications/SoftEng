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
    # disciplines/<discipline>/details/
    path(
        "disciplines/<slug:slug>/details/",
        discipline.DisciplineDetailView.as_view(),
        name="discipline-detail"
    ),
    # disciplines/<discipline>/remove/
    path(
        "disciplines/<slug:discipline>/remove/",
        discipline.DisciplineRemoveView.as_view(),
        name="discipline-remove"
    ),
    # disciplines/<discipline>/update/
    path(
        "disciplines/<slug:discipline>/update/",
        discipline.DisciplineUpdateView.as_view(),
        name="discipline-update"
    ),
    # disciplines/<discipline>/insert-required/
    path(
        "disciplines/<slug:discipline>/insert-required/",
        discipline.InsertRequiredDisciplineListView.as_view(),
        name="discipline-required-list"
    ),
    # disciplines/<discipline>/insert-required/<required>/
    path(
        "disciplines/<slug:discipline>/insert-required/<slug:required>/",
        discipline.InsertRequiredDisciplineView.as_view(),
        name="discipline-required-insert"
    ),
    # disciplines/<discipline>/remove-required/<required>/
    path(
        "disciplines/<slug:discipline>/remove-required/<slug:required>/",
        discipline.RemoveRequiredDisciplineView.as_view(),
        name="discipline-required-remove"
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
