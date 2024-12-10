from django import forms
from tock_time_app.common.mixins import MarkRequiredFieldsMixin
from tock_time_app.teams.models import Team


class TeamBaseForm(forms.ModelForm):
    """
    Base form for the Team model.
    Provides common configurations, including the fields 'name' and 'members'.
    """

    class Meta:
        model = Team
        fields = ['name', 'members',]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if user and hasattr(user, 'profile') and user.profile.friends.exists():
            friends_queryset = user.profile.friends.all()

            choices = [
                (user.pk, f'{user.username} - team\'s creator')
            ] + [
                (friend.user.pk, friend.user.username) for friend in friends_queryset
            ]
        else:
            choices = [(user.pk, f'{user.username} - team\'s creator')]

        self.fields['members'].choices = choices


class TeamCreateForm(MarkRequiredFieldsMixin, TeamBaseForm):
    """
    Form for creating a new team.
    Adds functionality to mark required fields.
    """

    # Indicator for required fields.
    required_indicator = '<span class="required-indicator">*</span>'


class TeamEditForm(TeamBaseForm):
    """ Form for editing an existing team. """

    pass