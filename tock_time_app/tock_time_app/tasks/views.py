from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from tock_time_app.tasks.forms import TaskCreateForm
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
    success_url = reverse_lazy('taskboard')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user

        return super().form_valid(form)