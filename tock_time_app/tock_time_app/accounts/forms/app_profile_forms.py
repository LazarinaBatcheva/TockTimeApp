"""
Forms for managing user profiles in the accounts app.
This module defines base and edit forms for the Profile model.
"""

from django import forms
from tock_time_app.accounts.models import Profile


class ProfileBaseForm(forms.ModelForm):
    """ Base form for the Profile model. """

    class Meta:
        model = Profile
        exclude = ['user', ]    # Excludes the 'user' field to prevent editing


class ProfileEditForm(ProfileBaseForm):
    """
    Form for editing profiles.
    Inherits:
        ProfileBaseForm: Adds no additional functionality beyond the base form.
    """

    pass
