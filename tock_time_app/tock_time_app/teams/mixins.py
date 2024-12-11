from django.urls import reverse_lazy


class UserFormKwargsMixin:
    """ A mixin to add the current user to the form kwargs. """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TeamSuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy(
            'teams-dashboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )