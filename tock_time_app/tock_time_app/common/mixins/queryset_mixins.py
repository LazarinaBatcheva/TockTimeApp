from django.apps import apps
from django.db.models import Q


class UserTeamsMixin:
    """ Mixin to filter teams the current user is associated with. """

    team_model = 'teams.Team'

    def get_queryset(self):
        """ Filters the teams based on the current user. """

        team = apps.get_model(self.team_model)

        return team.objects.filter(
            Q(members=self.request.user) | Q(created_by=self.request.user)
        ).distinct()


class UserTasksMixin:
    """
    Mixin to filter personal tasks for the current user, with optional filtering
    based on the 'task_status' attribute.
    """

    task_status = None

    def get_queryset(self):
        """ Filters the personal tasks based on the current user and task status. """

        personal_task = apps.get_model('tasks.PersonalTask')
        queryset = personal_task.objects.for_user(self.request.user)

        if self.task_status is not None:
            queryset = queryset.filter(is_completed=self.task_status)

        return queryset