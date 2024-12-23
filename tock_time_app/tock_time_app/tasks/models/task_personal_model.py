from django.contrib.auth import get_user_model
from django.db import models
from tock_time_app.tasks.choices import TaskPriorityChoices
from tock_time_app.tasks.managers import PersonalTaskManager
from tock_time_app.tasks.models import TaskBaseModel

UserModel = get_user_model()


class PersonalTask(TaskBaseModel):
    """
    Model for personal tasks, extending the shared TaskBaseModel.
    Includes fields for priority and the user who created the task.
    """

    priority = models.CharField(
        max_length=50,
        choices=TaskPriorityChoices.choices,
        default=TaskPriorityChoices.LOW,
    )

    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='created_personal_tasks',
    )

    objects = PersonalTaskManager()  # Custom manager for additional query functionality.
