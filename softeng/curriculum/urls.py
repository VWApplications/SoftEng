from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    # /
    path(
        "disciplines/",
        views.DisciplineListView.as_view(),
        name='discipline-list'
    ),
]
