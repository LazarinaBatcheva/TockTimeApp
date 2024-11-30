from django.db import models


class TaskPriorityChoices(models.TextChoices):
    """
    Enum-like class for defining task priority levels.
    Provides choices for task priority as a Django TextChoices enumeration.
    """

    HIGH = 'high', 'HIGH'
    MEDIUM = 'medium', 'MEDIUM'
    LOW = 'low', 'LOW'
