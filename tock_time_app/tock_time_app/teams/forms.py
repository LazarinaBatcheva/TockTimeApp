from django import forms

from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.teams.models import Team


class TeamBaseForm(forms.ModelForm):
    """
    Base form for the Team model.
    Provides common configurations, including the fields 'name' and 'members'.
    """

    class Meta:
        model = Team
        fields = ['name', 'members',]


class TeamCreateForm(MarkRequiredFieldsMixin, TeamBaseForm):
    """
    Form for creating a new team.
    Adds functionality to mark required fields.
    """

    # Indicator for required fields.
    required_indicator = '<span class="required-indicator">*</span>'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if user:
            choices = [
                (u.pk, f'{u.username} - team\'s creator' if u == user else u.username)
                for u in self.fields['members'].queryset
            ]

            self.fields['members'].choices = choices


class TeamEditForm(TeamBaseForm):
    """ Form for editing an existing team. """

    pass