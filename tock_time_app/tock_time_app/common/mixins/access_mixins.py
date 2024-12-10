from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from tock_time_app.accounts.models import Profile


class PermissionRequiredMixin:
    """
    General mixin to handle permission checks in `dispatch`.
    Other mixins can inherit this to reuse the logic.
    """

    def test_func(self):
        """
        Override this method in child mixins or views to implement custom permission logic.
        Must return True or False.
        """
        raise NotImplementedError("Subclasses must implement `test_func`.")

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)


class UserProfileAccessMixin(PermissionRequiredMixin):
    """
    Mixin to restrict access to a profile-related view.
    Ensures that only the owner of the profile can access it.
    """

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return self.request.user == profile.user


class UserTaskAccessMixin(PermissionRequiredMixin):
    """
    Mixin to restrict access to a task-related view.
    Ensures that only the owner of the task can access it.
    """

    def test_func(self):
        task = get_object_or_404(self.get_queryset().model, pk=self.kwargs['pk'])

        return self.request.user == task.created_by


class TeamObjectOwnerAccessMixin(PermissionRequiredMixin):
    """Mixin to ensure the user has access to objects they own."""

    owner_model = None   # Allows setting a specific model if not derived from the queryset.

    def test_func(self):
        model = self.owner_model or self.get_queryset().model
        obj = get_object_or_404(model, slug=self.kwargs['slug'])

        return obj.created_by == self.request.user


class ObjectCreatorMixin:
    """Mixin to provide context data for the creator of an object."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_creator'] = self.object.created_by == self.request.user

        return context
