from django import forms
from tock_time_app.accounts.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', ]


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['user', ]
        widgets = {
            'profile_picture': forms.FileInput(),
        }
