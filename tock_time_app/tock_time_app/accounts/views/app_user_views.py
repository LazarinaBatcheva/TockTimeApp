"""
Views for user authentication and registration in the accounts app.
This module provides views for user registration, login, and logout.
"""

from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tock_time_app.accounts.forms import AppUserCreationForm

# Get the custom user model
UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    """ Handles user registration."""

    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/user-register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Overrides the form_valid method to log in the user after successful registration.
        """

        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserLogInView(LoginView):
    """ Handles user login. """

    template_name = 'accounts/user-login.html'


class AppUserLogOutView(LogoutView):
    """ Handles user logout. """

    pass