class UserFormKwargsMixin:
    """ A mixin to add the current user to the form kwargs. """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs