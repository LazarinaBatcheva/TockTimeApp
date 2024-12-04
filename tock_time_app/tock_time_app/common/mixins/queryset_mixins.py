from django.apps import apps
from django.db.models import Q


class UserTeamsMixin:
    """ Mixin to filter teams the current user is associated with. """

    def get_queryset(self):
        Team = apps.get_model('teams.Team')

        return Team.objects.filter(
            Q(members=self.request.user) | Q(created_by=self.request.user)
        ).distinct()


class UserTasksMixin:
    """
    Mixin to filter personal tasks for the current user, with optional filtering
    based on the `task_status` attribute.
    """

    task_status = None

    def get_queryset(self):
        PersonalTask = apps.get_model('tasks.PersonalTask')
        queryset = PersonalTask.objects.for_user(self.request.user)

        if self.task_status is not None:
            queryset = queryset.filter(is_completed=self.task_status)

        return queryset