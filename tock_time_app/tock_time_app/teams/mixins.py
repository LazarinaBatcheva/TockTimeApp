from tock_time_app.teams.models import Team


class GetTeamQuerySetMixin:
    """
    Mixin to restrict the queryset to teams the current user is a member of.
    Ensures that users can only access teams they belong to.
    """

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)
