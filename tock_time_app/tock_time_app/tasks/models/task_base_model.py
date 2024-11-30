from django.db import models
from tock_time_app.common.mixins import DescriptionMixin, CreatedAtMixin


class TaskBaseModel(DescriptionMixin, CreatedAtMixin, models.Model):
    """
    Abstract base model for tasks.
    Provides common fields and behavior for task-related models, including:
    - Title: Name of the task.
    - Deadline: Date and time when the task should be completed.
    - Is Completed: Boolean flag to indicate task status.
    - Note: Optional text for additional task details.
    - Description and Created At: Added via mixins.
    """

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

    class Meta:
        abstract = True

        indexes = [
            models.Index(fields=['deadline', ]),
        ]
        ordering = ['deadline',]

    def __str__(self):
        return self.title
