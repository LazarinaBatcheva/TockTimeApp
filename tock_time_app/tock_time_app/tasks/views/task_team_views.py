from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tock_time_app.common.mixins.access_mixins import ObjectOwnerAccessMixin
from tock_time_app.tasks.forms import TeamTaskCreateForm
from tock_time_app.tasks.models import TeamTask
from tock_time_app.teams.models import Team


class TeamTaskCreateView(LoginRequiredMixin, ObjectOwnerAccessMixin, CreateView):
    """
    View for creating a new task within a team.
    Ensures the logged-in user is the owner of the team through ObjectOwnerAccessMixin.
    """

    model = TeamTask
    form_class = TeamTaskCreateForm
    template_name = 'tasks/tasks_team/team-task-create.html'
    owner_model = Team  # Specifies the model used to validate team ownership.

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