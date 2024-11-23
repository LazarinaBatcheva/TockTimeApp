from django import forms
from tock_time_app.teams.models import Team


class TeamBaseForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members',]


class TeamCreateForm(TeamBaseForm):
    pass