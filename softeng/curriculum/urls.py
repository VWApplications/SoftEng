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
    # disciplines/<slug-code>/details/
    path(
        "disciplines/<slug:slug>/details/",
        discipline.DisciplineDetailView.as_view(),
        name="discipline-detail"
    ),
    # extensions/
    path(
        "extensions/",
        curriculum.ExtensionListView.as_view(),
        name='extension-list'
    ),
    # multidisciplinary/
    path(
        "multidisciplinary/",
        curriculum.MultidisciplinaryListView.as_view(),
        name="multidisciplinary-list"
    ),
    # core_contents/
    path(
        "core_contents/",
        curriculum.CoreContentListView.as_view(),
        name="core-content-list"
    ),
]
