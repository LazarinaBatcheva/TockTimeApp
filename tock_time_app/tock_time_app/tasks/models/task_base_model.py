from django.db import models
from tock_time_app.common.mixins import DescriptionMixin, CreatedAtMixin, CreatedByMixin


class TaskBaseModel(DescriptionMixin, CreatedAtMixin, CreatedByMixin, models.Model):
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
