from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tock_time_app.common.mixins import UserProfileAccessMixin, UserTasksMixin
from tock_time_app.tasks.forms.task_personal_forms import PersonalTaskCreateForm, PersonalTaskEditForm
from tock_time_app.tasks.models import PersonalTask


class TaskboardView(LoginRequiredMixin, UserProfileAccessMixin, UserTasksMixin, ListView):
    """
    Displays a list of incomplete personal tasks for the logged-in user.
    Implements pagination with 5 tasks per page.
    """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/taskboard.html'
    paginate_by = 5
    task_status = False # Set the task status to incomplete


class PersonalTaskCreateView(LoginRequiredMixin, UserProfileAccessMixin, CreateView):
    """ Allows a logged-in user to create a new personal task. """

    model = PersonalTask
    form_class = PersonalTaskCreateForm
    template_name = 'tasks/tasks_personal/personal-task-create.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'personal-taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class PersonalTaskEditView(LoginRequiredMixin, UserProfileAccessMixin, UpdateView):
    """ Allows a logged-in user to edit an existing personal task. """

    model = PersonalTask
    form_class = PersonalTaskEditForm
    template_name = 'tasks/tasks_personal/personal-task-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'personal-taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class PersonalTaskDeleteView(LoginRequiredMixin, UserProfileAccessMixin, DeleteView):
    """ Allows a logged-in user to delete a personal task. """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/personal-task-delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'personal-taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class PersonalTaskDetailsView(LoginRequiredMixin, UserProfileAccessMixin, DetailView):
    """ Displays details for a specific personal task. """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/personal-task-details.html'


class UnarchiveTaskView(LoginRequiredMixin, UserProfileAccessMixin, UpdateView):
    """ Unarchives a task by marking it as incomplete. """

    model = PersonalTask
    fields = []  # No fields are needed because the update will be handled directly in form_valid.
    template_name = 'tasks/tasks_personal/archive.html'

    def form_valid(self, form):
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


class ArchivedTasksView(LoginRequiredMixin, UserProfileAccessMixin, UserTasksMixin, ListView):
    """
    Displays a list of completed personal tasks for the logged-in user.
    Implements pagination with 5 tasks per page.
    """

    model = PersonalTask
    template_name = 'tasks/tasks_personal/archive.html'
    paginate_by = 5
    task_status = True  # Set the task status to completed
