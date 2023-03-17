from django import forms
from django_select2 import forms as s2forms

from app.models import Agent


class AgentWidget(s2forms.ModelSelect2Widget):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {"style": "width: 200px"}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 1, "data-placeholder": self.empty_label}
        )
        return base_attrs

    empty_label = "Chercher un agent"
    queryset = Agent.objects.all()
    search_fields = [
        "last_name__icontains",
        "first_name__icontains",
        "registration_number__icontains",
    ]


class AgentSelectForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['id']

    id = forms.ModelChoiceField(
        widget=AgentWidget,
        queryset=Agent.objects.all())
