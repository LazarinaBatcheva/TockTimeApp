from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from tock_time_app.common.mixins import TeamObjectOwnerAccessMixin, ObjectCreatorMixin
from tock_time_app.tasks.forms import TeamTaskCreateForm, CreatorTeamTaskEditForm, MemberTeamTaskForm
from tock_time_app.tasks.mixins import TeamTaskFormMixin
from tock_time_app.tasks.models import TeamTask
from tock_time_app.teams.models import Team


class TeamTaskCreateView(LoginRequiredMixin, TeamObjectOwnerAccessMixin, TeamTaskFormMixin, CreateView):
    """
    View for creating a new task within a team.
    Ensures the logged-in user is the owner of the team through ObjectOwnerAccessMixin.
    """

    model = TeamTask
    form_class = TeamTaskCreateForm
    template_name = 'tasks/tasks_team/team-task-create.html'
    owner_model = Team  # Specifies the model used to validate team ownership.

    def get_team(self):
        return get_object_or_404(Team, slug=self.kwargs['slug'])

    def form_valid(self, form):
        """
        Custom logic for handling the form submission:
        - Associates the created task with the specified team.
        - Sets the logged-in user as the creator of the task.
        """

        task = form.save(commit=False)
        task.team = get_object_or_404(Team, slug=self.kwargs['slug'])
        task.created_by = self.request.user
        task.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'team-details',
            kwargs={
                'username': self.kwargs['username'],
                'slug': self.kwargs['slug'],
            }
        )


class TeamTaskEditView(LoginRequiredMixin, ObjectCreatorMixin, TeamTaskFormMixin, UpdateView):
    """
    View for editing a team task.
    Ensures the user has the proper permissions to edit the task.
    """

    model = TeamTask
    template_name = 'tasks/tasks_team/team-task-edit.html'
    owner_model = Team  # Specifies the model used to validate team ownership.
    context_object_name = 'task'

    def get_form_class(self):
        """ Dynamically return the form class based on the user's role and permissions. """

        task = self.get_object()

        # Check if the user has permission to edit tasks or is the task creator
        if self.request.user == task.created_by:
            return CreatorTeamTaskEditForm

        # Check if the user is assigned to the task
        if self.request.user in task.assigned_to.all():
            return MemberTeamTaskForm

        # If none of the above, raise a PermissionError
        raise PermissionError('You do not have permission to edit this task.')

    def get_success_url(self):
        return reverse_lazy(
            'team-details',
            kwargs={
                'username': self.kwargs['username'],
                'slug': self.kwargs['slug'],
            }
        )


class TeamTaskDeleteView(LoginRequiredMixin, ObjectCreatorMixin, DeleteView):
    model = TeamTask
    template_name = 'tasks/tasks_team/team-task-delete.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy(
            'team-details',
            kwargs={
                'username': self.kwargs['username'],
                'slug': self.kwargs['slug'],
            }
        )


class TasksForApproveView(LoginRequiredMixin, ListView):
    """ View for displaying tasks that require approval. """

    model = TeamTask
    template_name = 'tasks/tasks_team/tasks-for-approve.html'
    context_object_name = 'tasks'
    paginate_by = 3

    def get_queryset(self):
        team_slug = self.kwargs['slug']
        team = get_object_or_404(Team, slug=team_slug)

        return TeamTask.objects.filter(team=team, is_completed=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = get_object_or_404(Team, slug=self.kwargs['slug'])

        return context


class TaskRejectApproveView(LoginRequiredMixin, UpdateView):
    """
    View for rejecting a task approval.
    Marks the task as uncompleted and redirects to team details.
    """

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(TeamTask, pk=self.kwargs['pk'])

        task.is_completed = False
        task.save()

        # Redirect to success URL
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            'tasks-for-approve',
            kwargs={
                'username': self.kwargs['username'],
                'slug': self.kwargs['slug'],
            }
        )


class TeamTaskDetailsView(LoginRequiredMixin, DetailView):
    """
    View for displaying details of a team task.
    """

    model = TeamTask
    template_name = 'tasks/tasks_team/team-task-details.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        """
        Custom logic to retrieve the task object:
        - Ensures the task belongs to the specified team.
        - Validates that the user has access to the task.
        """

        task = super().get_object(queryset)
        team = get_object_or_404(Team, slug=self.kwargs['slug'])

        if task.team != team:
            # If the task does not belong to the team, return None to trigger a 404 error.
            return None

        return task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['team'] = get_object_or_404(Team, slug=self.kwargs['slug'])
        context['is_creator'] = self.request.user == task.created_by

        return context
