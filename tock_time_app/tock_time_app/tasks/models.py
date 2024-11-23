from django.contrib.auth import get_user_model
from django.db import models
from tock_time_app.common.mixins import DescriptionMixin, CreatedAtMixin
from tock_time_app.tasks.choices import TaskPriorityChoices

UserModel = get_user_model()


class Task(DescriptionMixin, CreatedAtMixin, models.Model):
    title = models.CharField(
        max_length=100,
    )

    deadline = models.DateTimeField()

    is_completed = models.BooleanField(
        default=False,
    )

    note = models.TextField(
        null=True,
        blank=True,
    )

    priority = models.CharField(
        max_length=50,
        choices=TaskPriorityChoices.choices,
        default=TaskPriorityChoices.LOW,
    )

    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='created_tasks',
    )

    assigned_to = models.ManyToManyField(
        to=UserModel,
        related_name='assigned_tasks',
        blank=True,
    )

    team = models.ForeignKey(
        to='teams.Team',
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True,
        help_text='If this task is for a team, select the team here.',
    )

    class Meta:
        permissions = [
            ('assign_task', 'Can assign task to user'),
        ]
        indexes = [
            models.Index(fields=['deadline', ]),
        ]
        ordering = ['deadline',]

    def __str__(self):
        return self.title
