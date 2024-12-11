from django.db import models
from django.utils.timezone import now


class PersonalTaskManager(models.Manager):
    """
    Custom manager for the PersonalTask model.
    Provides additional query methods specific to personal tasks.
    """

    def for_user(self, user):
        """Returns all tasks for a specific user."""

        return self.filter(created_by=user)

    def mark_failed_for_user(self, user):
        """ Marks all overdue tasks as failed for a specific user and archives them. """

        overdue_tasks = self.filter(deadline__lt=now(), is_completed=False, created_by=user)

        return overdue_tasks.update(note='FAILED', is_completed=True)
