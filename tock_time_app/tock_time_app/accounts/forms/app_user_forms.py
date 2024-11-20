from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'ex. johndoe123'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ex. johndoe@mail.com'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password1'].help_text = None

        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['password2'].help_text = None


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

