from django import forms
from django.shortcuts import get_object_or_404

from app.models import Agent


class AgentSelectForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = [(agent.id, f'{agent.last_name} {agent.first_name} - {agent.registration_number}')
                   for agent in Agent.objects.all()]

        self.fields['id'] = forms.ChoiceField(choices=choices, label="Choix")
