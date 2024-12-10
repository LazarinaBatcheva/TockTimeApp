class TeamTaskFormMixin:
    """
    Mixin to pass the team associated with a task to the form for filtering.
    """

    def get_form_kwargs(self):
        """ Add the team to the form kwargs. """
        kwargs = super().get_form_kwargs()
        task = self.get_object()
        if hasattr(task, 'team'):
            kwargs['team'] = task.team
        return kwargs