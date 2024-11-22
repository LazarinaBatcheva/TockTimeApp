from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tock_time_app.common.mixins import PlaceholderMixin, NoHelpTextMixin

UserModel = get_user_model()


class AppUserCreationForm(PlaceholderMixin, NoHelpTextMixin, UserCreationForm):
    placeholder_fields = {
        'password1': 'Enter password',
        'password2': 'Confirm password',
    }

    help_text_fields = ['password1', 'password2']

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ex. johndoe123'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ex. johndoe@mail.com'}),
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

