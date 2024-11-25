# Personal tasks views
from tock_time_app.tasks.views.task_personal_views import TaskboardView, PersonalTaskCreateView, PersonalTaskEditView, \
    PersonalTaskDeleteView, PersonalTaskDetailsView
# Team tasks views
from .task_team_views import TeamTaskCreateView

__all__ = [
    # Personal tasks views
    'TaskboardView',
    'PersonalTaskCreateView',
    'PersonalTaskEditView',
    'PersonalTaskDeleteView',
    'PersonalTaskDetailsView',

    # Team tasks views
    'TeamTaskCreateView',
]

