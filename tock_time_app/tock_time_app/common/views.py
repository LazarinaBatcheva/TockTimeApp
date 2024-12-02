from django.views.generic import TemplateView
from tock_time_app.common.mixins import UserTeamsMixin, UserTasksMixin


class HomePageView(TemplateView, UserTeamsMixin, UserTasksMixin):
    """
    View for rendering the home page.
    Displays personalized data such as incomplete personal tasks and teams the user is associated with.
    Inherits from TemplateView to handle rendering a static template.
    """

    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        """ Adds context data for the home page template. """

        context = super().get_context_data(**kwargs)

        # Set the task_status to filter for incomplete tasks
        self.task_status = False
        context['personal_tasks'] = UserTasksMixin.get_queryset(self)

        # Retrieve teams using UserTeamsMixin
        context['teams'] = UserTeamsMixin.get_queryset(self)

        return context
