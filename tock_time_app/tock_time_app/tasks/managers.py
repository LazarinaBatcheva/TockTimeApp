from django.db import models


class PersonalTaskManager(models.Manager):
    def for_user(self, user):
        """Returns all tasks for a specific user."""
        return self.filter(created_by=user)

    def uncompleted_for_user(self, user):
        """Returns the uncompleted tasks for a specific user."""
        return self.filter(created_by=user, is_completed=False)

