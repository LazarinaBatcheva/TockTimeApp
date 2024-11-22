from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from tock_time_app.accounts.forms import ProfileEditForm
from tock_time_app.accounts.models import Profile
from tock_time_app.common.mixins import UserProfileAccessMixin

UserModel = get_user_model()


class ProfileEditView(LoginRequiredMixin, UserProfileAccessMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )


class ProfileDeleteView(LoginRequiredMixin, UserProfileAccessMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('profile-deleted-page')


class ProfileDeletedPageView(TemplateView):
    template_name = 'accounts/profile-deleted-page.html'


class ProfileDetailsView(LoginRequiredMixin, UserProfileAccessMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

