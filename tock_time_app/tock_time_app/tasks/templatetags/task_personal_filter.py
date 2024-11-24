from django import template
from tock_time_app.tasks.models import Task

register = template.Library()


@register.filter
def personal_task_count(user):
    if not user.is_authenticated:
        return 0
    return (Task.objects
            .filter(created_by=user, team__isnull=True)
            .count())

