from django.views.generic import ListView
from curriculum.models import Extension, Multidisciplinary


class ExtensionListView(ListView):
    """
    Page to list all extension activities.
    """

    model = Extension
    template_name = "curriculum/extensions.html"
    context_object_name = "extensions"


class MultidisciplinaryListView(ListView):
    """
    Page to list all multidisciplinary activities.
    """

    model = Multidisciplinary
    template_name = "curriculum/multidisciplinary.html"
    context_object_name = "multidisciplinary_disciplines"
