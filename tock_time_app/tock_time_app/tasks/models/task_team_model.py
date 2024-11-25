from django.contrib.auth import get_user_model
from django.db import models
from tock_time_app.tasks.models import TaskBaseModel

UserModel = get_user_model()


class TeamTask(TaskBaseModel):
    assigned_to = models.ManyToManyField(
        to=UserModel,
        related_name='assigned_tasks',
    )

    team = models.ForeignKey(
        to='teams.Team',
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    class Meta:
        permissions = [
            ('assign_task', 'Can assign task to user'),
        ]
