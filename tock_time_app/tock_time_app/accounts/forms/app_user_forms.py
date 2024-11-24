from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tock_time_app.common.mixins import PlaceholderMixin, NoHelpTextMixin
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin

UserModel = get_user_model()


class AppUserCreationForm(MarkRequiredFieldsMixin, PlaceholderMixin, NoHelpTextMixin, UserCreationForm):
    placeholder_fields = {
        'username': 'ex. johndoe123',
        'email': 'ex. johndoe@mail.com',
        'password1': 'Enter password',
        'password2': 'Confirm password',
    }

    help_text_fields = ['password1', 'password2']

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', ]


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

