from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tock_time_app.common.mixins import UserProfileAccessMixin
from tock_time_app.tasks.forms import TaskCreateForm, TaskEditForm
from tock_time_app.tasks.models import Task


class TaskboardView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/taskboard.html'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/task-create.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TaskEditView(LoginRequiredMixin, UserProfileAccessMixin, UpdateView):
    model = Task
    form_class = TaskEditForm
    template_name = 'tasks/task-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TaskDeleteView(LoginRequiredMixin, UserProfileAccessMixin, DeleteView):
    model = Task
    template_name = 'tasks/task-delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'taskboard',
            kwargs={
                'username': self.kwargs['username'],
            }
        )


class TaskDetailsView(LoginRequiredMixin, UserProfileAccessMixin, DetailView):
    model = Task
    template_name = 'tasks/task-details.html'