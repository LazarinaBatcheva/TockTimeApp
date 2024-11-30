from django.contrib.auth import get_user_model
from django.db import models
from tock_time_app.tasks.models import TaskBaseModel

UserModel = get_user_model()


class TeamTask(TaskBaseModel):
    """
    Model representing tasks assigned to a team or team members.
    Extends TaskBaseModel and includes fields for assigned users, team, and creator.
    """

    assigned_to = models.ManyToManyField(
        to=UserModel,
        related_name='assigned_tasks',
    )

    team = models.ForeignKey(
        to='teams.Team',
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='created_team_tasks',
    )

    class Meta:
        permissions = [
            ('assign_task', 'Can assign task to user'),
        ]
