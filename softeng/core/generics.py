from django.views.generic import DeleteView
from django.shortcuts import redirect


class ObjectRedirectView(DeleteView):
    """
    Redirect to success url after perform some action.
    """

    def post(self, request, *args, **kwargs):
        """
        Post method to perform some action.
        """

        return self.action(request, *args, **kwargs)

    def action(self, request, *args, **kwargs):
        """
        Do some action
        """

        self.object = self.get_object()
        success_url = self.get_success_url()
        return redirect(success_url)
