from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tock_time_app.common.mixins import UserTasksMixin, UserTaskAccessMixin, ObjectCreatorMixin
from tock_time_app.tasks.forms import PersonalTaskCreateForm, PersonalTaskEditForm
from tock_time_app.tasks.mixins import PersonalTasksSuccessUrlMixin
from tock_time_app.tasks.models import PersonalTask


class TaskboardView(LoginRequiredMixin, UserTasksMixin, ListView):
    """
    Displays a list of incomplete personal tasks for the logged-in user.
    Implements pagination with 5 tasks per page.
    """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/taskboard.html'
    paginate_by = 5
    task_status = False  # Set the task status to incomplete

    def get_queryset(self):
        # Mark overdue tasks as failed
        PersonalTask.objects.mark_failed_for_user(self.request.user)

        return super().get_queryset()


class PersonalTaskCreateView(LoginRequiredMixin, PersonalTasksSuccessUrlMixin, CreateView):
    """ Allows a logged-in user to create a new personal task. """

    model = PersonalTask
    form_class = PersonalTaskCreateForm
    template_name = 'tasks/tasks_personal/personal-task-create.html'

    def form_valid(self, form):
        """ Set the current user as the creator of the task. """

        task = form.save(commit=False)
        task.created_by = self.request.user

        return super().form_valid(form)


class PersonalTaskEditView(LoginRequiredMixin, UserTaskAccessMixin, PersonalTasksSuccessUrlMixin, UpdateView):
    """ Allows a logged-in user to edit an existing personal task. """

    model = PersonalTask
    form_class = PersonalTaskEditForm
    template_name = 'tasks/tasks_personal/personal-task-edit.html'
    context_object_name = 'task'


class PersonalTaskDeleteView(LoginRequiredMixin, UserTaskAccessMixin, PersonalTasksSuccessUrlMixin, DeleteView):
    """ Allows a logged-in user to delete a personal task. """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/personal-task-delete.html'


class PersonalTaskDetailsView(LoginRequiredMixin, UserTaskAccessMixin, ObjectCreatorMixin, DetailView):
    """ Displays details for a specific personal task. """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/personal-task-details.html'
    context_object_name = 'task'


class UnarchiveTaskView(LoginRequiredMixin, UserTaskAccessMixin, UpdateView):
    """ Unarchives a task by marking it as incomplete. """

    model = PersonalTask
    fields = []  # No fields are needed because the update will be handled directly in form_valid.
    template_name = 'tasks/tasks_personal/archive.html'

    def form_valid(self, form):
        """ Mark the task as incomplete. """

        task = form.save(commit=False)
        task.is_completed = False
        task.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'personal-tasks-archive',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class ArchivedTasksView(LoginRequiredMixin, UserTasksMixin, ListView):
    """
    Displays a list of completed personal tasks for the logged-in user.
    Implements pagination with 5 tasks per page.
    """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/archive.html'
    paginate_by = 5
    task_status = True  # Set the task status to completed
