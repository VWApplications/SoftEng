from django.urls import path
from .views import swebok, content

app_name = 'knowledge'

urlpatterns = [
    # swebok/
    path(
        "swebok/",
        swebok.SwebokListView.as_view(),
        name='swebok-list'
    ),
    # swebok/<topic>/details/
    path(
        "swebok/<slug:knowledge>/<slug:topic>/details/",
        swebok.SwebokDetailView.as_view(),
        name="swebok-detail"
    ),
    # swebok/<knowledge>/<topic>/<subtopic>/insert/
    path(
        "swebok/<slug:knowledge>/<slug:topic>/<slug:subtopic>/insert/",
        content.InsertContentListView.as_view(),
        name="disciplines"
    ),
    # swebok/<knowledge>/<topic>/<subtopic>/insert-content/
    path(
        "swebok/<slug:knowledge>/<slug:topic>/<slug:subtopic>/<slug:discipline>/insert/",
        content.InsertContentView.as_view(),
        name="insert"
    ),
]
