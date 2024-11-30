from django.shortcuts import get_object_or_404
from tock_time_app.accounts.models import Profile


class UserProfileAccessMixin:
    """
    Mixin to restrict access to a profile-related view.
    Ensures that only the owner of the profile can access it.
    """

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class ObjectOwnerAccessMixin:
    """Mixin to ensure the user has access to objects they own."""

    owner_model = None   # Allows setting a specific model if not derived from the queryset.

    def test_func(self):
        model = self.owner_model or self.get_queryset().model
        obj = get_object_or_404(model, slug=self.kwargs['slug'])
        return obj.created_by == self.request.user
