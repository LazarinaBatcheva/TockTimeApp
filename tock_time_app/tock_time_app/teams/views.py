from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tock_time_app.common.mixins import UserTeamsMixin
from tock_time_app.common.mixins.access_mixins import TeamObjectOwnerAccessMixin
from tock_time_app.tasks.models import TeamTask
from tock_time_app.teams.forms import TeamCreateForm, TeamEditForm
from tock_time_app.mixins import UserFormKwargsMixin
from tock_time_app.teams.models import Team


class TeamsDashboardView(LoginRequiredMixin, UserTeamsMixin, ListView):
    """
    View for displaying a list of teams the logged-in user is a member of.
    Implements pagination with 5 teams per page.
    """

    model = Team
    template_name = 'teams/teams-dashboard.html'
    paginate_by = 5


class TeamCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    """
    View for creating a new team.
    Allows the logged-in user to create a team and automatically adds them as a member.
    """

    model = Team
    form_class = TeamCreateForm
    template_name = 'teams/team-create.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.created_by = self.request.user
        team.save()

        if not team.members.filter(pk=self.request.user.pk).exists():
            team.members.add(self.request.user)

        form.save_m2m()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'teams-dashboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TeamEditView(LoginRequiredMixin, TeamObjectOwnerAccessMixin, UserFormKwargsMixin, UpdateView):
    """
    View for editing a team.
    Allows the team creator to update the team's details.
    """

    model = Team
    form_class = TeamEditForm
    template_name = 'teams/team-edit.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        new_members = form.cleaned_data.get('members', [])

        team.members.set(new_members)
        team.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'teams-dashboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TeamDeleteView(LoginRequiredMixin, TeamObjectOwnerAccessMixin, DeleteView):
    """
    View for deleting a team.
    Allows the team creator to delete the team.
    """

    model = Team
    template_name = 'teams/team-delete.html'
    success_url = reverse_lazy('teams-dashboard')


class TeamDetailsView(LoginRequiredMixin, UserTeamsMixin, DetailView):
    """
    View for displaying the details of a specific team.
    Restricts access to teams the current user is a member of.
    """

    model = Team
    template_name = 'teams/team-details.html'
    context_object_name = 'team'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = TeamTask.objects.filter(team=self.object, is_completed=False)
        paginator = Paginator(tasks, self.paginate_by)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['team_tasks'] = page_obj
        context['is_creator'] = self.object.created_by == self.request.user
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()

        return context
