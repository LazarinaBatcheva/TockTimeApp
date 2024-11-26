"""
Views for managing user profiles in the accounts app.
This module provides views for editing, deleting, and viewing user profiles.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from tock_time_app.accounts.forms import ProfileEditForm
from tock_time_app.accounts.models import Profile
from tock_time_app.common.mixins import UserProfileAccessMixin

UserModel = get_user_model()


class ProfileEditView(LoginRequiredMixin, UserProfileAccessMixin, UpdateView):
    """ View for editing user profiles. """

    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    # Returns the URL to redirect to after successfully updating the profile.
    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )


class ProfileDeleteView(LoginRequiredMixin, UserProfileAccessMixin, DeleteView):
    """ View for deleting user profiles. """

    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('profile-deleted-page')


class ProfileDeletedPageView(TemplateView):
    """ View for displaying a confirmation page after a profile is deleted. """

    template_name = 'accounts/profile-deleted-page.html'


class ProfileDetailsView(LoginRequiredMixin, UserProfileAccessMixin, DetailView):
    """ View for displaying user profile details. """

    model = UserModel
    template_name = 'accounts/profile-details.html'

