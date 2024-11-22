from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from tock_time_app.tasks.models import Task


class TaskboardView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/taskboard.html'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

