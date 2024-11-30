from django import forms

from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.teams.models import Team


class TeamBaseForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members',]


class TeamCreateForm(MarkRequiredFieldsMixin, TeamBaseForm):
    required_indicator = '<span class="required-indicator">*</span>'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['members'].queryset = self.fields['members'].queryset.exclude(pk=user.pk)