from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from tock_time_app.teams.forms import TeamCreateForm
from tock_time_app.teams.models import Team


class TeamsDashboardView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'teams/teams-dashboard.html'
    paginate_by = 6

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamCreateForm
    template_name = 'teams/team-create.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.created_by = self.request.user
        team.save()

        team.members.add(self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'teams-dashboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )