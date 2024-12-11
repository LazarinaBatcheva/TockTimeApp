from django.urls import reverse_lazy


class PersonalTasksSuccessUrlMixin:
    """
    Mixin to provide a dynamic success URL for personal tasks.
    Redirects to the personal taskboard after a successful operation.
    """

    def get_success_url(self):
        return reverse_lazy(
            'personal-taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TeamTasksSuccessUrlMixin:
    """
   Mixin to provide a dynamic success URL for team tasks.
   Redirects to the team details page after a successful operation.
   """

    def get_success_url(self):
        return reverse_lazy(
            'team-details',
            kwargs={
                'username': self.kwargs['username'],
                'slug': self.kwargs['slug'],
            }
        )


class TeamTaskFormMixin:
    """
    Mixin to pass the team associated with a task to the form for filtering.
    Ensures the form receives the team context for task-related operations.
    """

    def get_form_kwargs(self):
        """ Add the team to the form kwargs. """
        kwargs = super().get_form_kwargs()
        task = self.get_object()

        if hasattr(task, 'team'):
            kwargs['team'] = task.team

        return kwargs