from django.shortcuts import get_object_or_404
from tock_time_app.accounts.models import Profile


class UserProfileAccessMixin:
    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class ObjectOwnerAccessMixin:
    """Mixin to ensure the user has access to objects they own."""
    def test_func(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        return obj.created_by == self.request.user