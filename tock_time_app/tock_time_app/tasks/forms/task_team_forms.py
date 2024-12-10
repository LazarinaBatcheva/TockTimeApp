from django import forms
from tock_time_app.common.mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import TeamTask


class TeamTaskBaseForm(forms.ModelForm):
    class Meta:
        model = TeamTask
        fields = ['title', 'deadline', 'assigned_to', 'description', 'note', 'is_completed']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'assigned_to': forms.SelectMultiple(attrs={'size': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super().__init__(*args, **kwargs)

        if team:
            self.fields['assigned_to'].queryset = team.members.all()


class TeamTaskCreateForm(MarkRequiredFieldsMixin, TeamTaskBaseForm):
    """
    Form for creating a TeamTask.
    Adds functionality to mark required fields with an indicator and provides custom widgets.
    """

    required_indicator = '<span class="required-indicator">*</span>'


class CreatorTeamTaskEditForm(TeamTaskBaseForm):
    """ Form for the creator to edit all fields of a TeamTask. """

    class Meta(TeamTaskBaseForm.Meta):
        fields = ['deadline', 'assigned_to', 'description', 'note', 'is_completed']


class MemberTeamTaskForm(TeamTaskBaseForm):
    """ Form for team members to edit only limited fields of a TeamTask. """
    class Meta(TeamTaskBaseForm.Meta):
        model = TeamTask
        fields = ['note', 'is_completed']