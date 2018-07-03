from django import forms


class DisciplineForm(forms.Form):
    """
    Form to create/update a discipline
    """

    title = forms.CharField()
    code = forms.IntegerField()
    description = forms.CharField()
    classification = forms.CharField()
    flow = forms.CharField()
    core = forms.CharField()
