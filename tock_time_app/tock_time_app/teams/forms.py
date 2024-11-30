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

    Adds functionality to mark required fields and filters the 'members'
    queryset to exclude the current user.
    """

    required_indicator = '<span class="required-indicator">*</span>'    # Indicator for required fields.

    def __init__(self, *args, **kwargs):
        """
        Custom initialization for the form.
        Excludes the currently logged-in user from the 'members' field queryset.
        """

        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['members'].queryset = self.fields['members'].queryset.exclude(pk=user.pk)