from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    # disciplines/
    path(
        "disciplines/",
        views.DisciplineListView.as_view(),
        name='discipline-list'
    ),
    # disciplines/<slug-code>/details/
    path(
        "disciplines/<slug:slug>/details/",
        views.DisciplineDetailView.as_view(),
        name="discipline-detail"
    ),
]
