from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from tock_time_app.common.mixins.access_mixins import ObjectOwnerAccessMixin
from tock_time_app.teams.forms import TeamCreateForm, TeamTaskCreateForm
from tock_time_app.teams.mixins import GetTeamQuerySetMixin
from tock_time_app.teams.models import Team


class TeamsDashboardView(LoginRequiredMixin, GetTeamQuerySetMixin,  ListView):
    model = Team
    template_name = 'teams/teams-dashboard.html'
    paginate_by = 6


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


# class TeamTaskCreateView(LoginRequiredMixin, ObjectOwnerAccessMixin, CreateView):
#     model = Task
#     form_class = TeamTaskCreateForm
#     template_name = 'teams/team-task-create.html'
#     owner_model = Team
#
#     def form_valid(self, form):
#         task = form.save(commit=False)
#         task.team = get_object_or_404(Team, slug=self.kwargs['slug'])
#         task.created_by = self.request.user
#         task.save()
#
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy(
#             'team-details',
#             kwargs={
#                 'username': self.kwargs['username'],
#                 'slug': self.kwargs['slug'],
#             }
#         )


# class TeamDetailsView(LoginRequiredMixin, GetTeamQuerySetMixin, DetailView):
#     model = Team
#     template_name = 'teams/team-details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['team_tasks'] = Task.objects.filter(team=self.object)
#         return context
