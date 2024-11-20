from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tock_time_app.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/user-register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserLogInView(LoginView):
    template_name = 'accounts/user-login.html'


class AppUserLogOutView(LogoutView):
    pass