from django import forms
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import TeamTask


class TeamTaskBaseForm(forms.ModelForm):
    class Meta:
        model = TeamTask
        fields = ['title', 'deadline', 'assigned_to', 'description', 'note', 'is_approved']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'assigned_to': forms.SelectMultiple(attrs={'size': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and hasattr(user, 'profile'):
            self.fields['assigned_to'].queryset = user.profile.friends.all()


class TeamTaskCreateForm(MarkRequiredFieldsMixin, TeamTaskBaseForm):
    """
    Form for creating a TeamTask.
    Adds functionality to mark required fields with an indicator and provides custom widgets.
    """

    required_indicator = '<span class="required-indicator">*</span>'

    class Meta(TeamTaskBaseForm.Meta):
        exclude = ['is_approved',]


class TeamTaskEditForm(TeamTaskBaseForm):
    """
    Form for editing a TeamTask.
    Provides custom widgets.
    """

    class Meta(TeamTaskBaseForm.Meta):
        fields = ['deadline', 'assigned_to', 'description', 'note', 'is_completed', 'is_approved']

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)

        super().__init__(*args, **kwargs)

        if team:
            self.fields['assigned_to'].queryset = team.members.all()