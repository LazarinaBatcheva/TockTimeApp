from django.db import models


class TaskPriorityChoices(models.TextChoices):
    HIGH = 'high', 'HIGH'
    MEDIUM = 'medium', 'MEDIUM'
    LOW = 'low', 'LOW'
