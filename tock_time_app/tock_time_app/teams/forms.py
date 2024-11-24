from django import forms
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import Task
from tock_time_app.teams.models import Team


class TeamBaseForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members',]


class TeamCreateForm(TeamBaseForm):
    pass


class TeamTaskCreateForm(MarkRequiredFieldsMixin, forms.ModelForm):
    required_indicator = '<span class="required-indicator">*</span>'

    class Meta:
        model = Task
        fields = ['title', 'priority', 'deadline', 'assigned_to', 'description', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'assigned_to': forms.SelectMultiple(attrs={'size': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }