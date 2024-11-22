from django.shortcuts import get_object_or_404
from tock_time_app.accounts.models import Profile


class UserProfileAccessMixin:
    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user
