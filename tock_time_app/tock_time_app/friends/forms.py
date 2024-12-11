from django import forms
from tock_time_app.friends.models import FriendRequest


class FriendRequestForm(forms.ModelForm):
    """ Form for creating a friend request. """

    class Meta:
        model = FriendRequest
        fields = ['receiver',]