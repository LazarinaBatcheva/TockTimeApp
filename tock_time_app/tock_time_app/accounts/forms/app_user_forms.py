"""
Forms for user creation and update in the accounts app.

This module defines forms for creating and updating users,
customized with mixins for placeholders and help text.
"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tock_time_app.common.mixins import PlaceholderMixin, NoHelpTextMixin

UserModel = get_user_model()


class AppUserCreationForm(PlaceholderMixin, NoHelpTextMixin, UserCreationForm):
    """ Custom user creation form.
    Inherits:
        PlaceholderMixin: Adds placeholders to form fields.
        NoHelpTextMixin: Removes help text from specified fields.
        UserCreationForm: Django's built-in form for user creation.
    """

    placeholder_fields = {
        'username': 'ex. johndoe123',
        'email': 'ex. johndoe@mail.com',
        'password1': 'Enter password',
        'password2': 'Confirm password',
    }

    help_text_fields = ['password1', 'password2']   # Fields where help text will be removed

    class Meta(UserCreationForm.Meta):
        model = UserModel   # Custom user model
        fields = ['username', 'email', ]


class AppUserChangeForm(UserChangeForm):
    """
    Custom user change form.
    Inherits:
        UserChangeForm: Django's built-in form for changing user details.
    """

    class Meta(UserChangeForm.Meta):
        model = UserModel   # Custom user model

