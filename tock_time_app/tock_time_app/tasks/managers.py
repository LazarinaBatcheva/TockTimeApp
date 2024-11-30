from django.db import models


class PersonalTaskManager(models.Manager):
    """
    Custom manager for the PersonalTask model.
    Provides additional query methods specific to personal tasks.
    """

    def for_user(self, user):
        """Returns all tasks for a specific user."""

        return self.filter(created_by=user)