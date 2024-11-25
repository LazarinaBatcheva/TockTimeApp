from django.db import models
from tock_time_app.tasks.choices import TaskPriorityChoices
from tock_time_app.tasks.managers import PersonalTaskManager
from tock_time_app.tasks.models import TaskBaseModel


class PersonalTask(TaskBaseModel):
    priority = models.CharField(
        max_length=50,
        choices=TaskPriorityChoices.choices,
        default=TaskPriorityChoices.LOW,
    )

    objects = PersonalTaskManager()
