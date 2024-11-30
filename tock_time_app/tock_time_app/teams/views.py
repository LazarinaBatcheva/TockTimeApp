from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from tock_time_app.tasks.models import TeamTask
from tock_time_app.teams.forms import TeamCreateForm
from tock_time_app.teams.mixins import GetTeamQuerySetMixin
from tock_time_app.teams.models import Team


class TeamsDashboardView(LoginRequiredMixin, GetTeamQuerySetMixin,  ListView):
    model = Team
    template_name = 'teams/teams-dashboard.html'
    paginate_by = 6

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamCreateForm
    template_name = 'teams/team-create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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


class TeamDetailsView(LoginRequiredMixin, GetTeamQuerySetMixin, DetailView):
    model = Team
    template_name = 'teams/team-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_tasks'] = TeamTask.objects.filter(team=self.object)

        return context
