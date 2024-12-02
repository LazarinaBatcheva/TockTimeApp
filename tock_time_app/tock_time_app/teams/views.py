from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from tock_time_app.common.mixins import UserTeamsMixin
from tock_time_app.tasks.models import TeamTask
from tock_time_app.teams.forms import TeamCreateForm
from tock_time_app.teams.models import Team


class TeamsDashboardView(LoginRequiredMixin, UserTeamsMixin, ListView):
    """
    View for displaying a list of teams the logged-in user is a member of.
    Implements pagination with 5 teams per page.
    """

    model = Team
    template_name = 'teams/teams-dashboard.html'
    paginate_by = 5

    def get_object(self, queryset=None):
        """
        Ensures the user can access the requested team.
        """
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])


class TeamCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new team.
    Allows the logged-in user to create a team and automatically adds them as a member.
    """

    model = Team
    form_class = TeamCreateForm
    template_name = 'teams/team-create.html'

    def get_form_kwargs(self):
        """
        Passes the current user to the form's constructor for filtering the 'members' field.
        """

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


class TeamDetailsView(LoginRequiredMixin, UserTeamsMixin, DetailView):
    """
    View for displaying the details of a specific team.
    Restricts access to teams the current user is a member of.
    """

    model = Team
    template_name = 'teams/team-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_tasks'] = TeamTask.objects.filter(team=self.object)

        return context
