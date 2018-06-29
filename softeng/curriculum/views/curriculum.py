from django.views.generic import ListView
from curriculum.models import CoreContent, Extension


class ExtensionListView(ListView):
    """
    Page to list all extension activities.
    """

    template_name = "curriculum/extensions.html"
    context_object_name = "extensions"

    def get_queryset(self):
        """
        Get all the extensions.
        """

        extensions = Extension().get_instance()

        return extensions


class CoreContentListView(ListView):
    """
    Page to list all core contents.
    """

    template_name = "curriculum/core_content.html"
    context_object_name = "core_contents"

    def get_queryset(self):
        """
        Get the multidisciplinary model.
        """

        core_contents = CoreContent().get_instance()

        return core_contents
