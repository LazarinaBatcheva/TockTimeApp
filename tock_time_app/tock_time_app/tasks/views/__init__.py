# Personal tasks views
from tock_time_app.tasks.views.task_personal_views import TaskboardView, PersonalTaskCreateView, ArchivedTasksView, \
    PersonalTaskEditView, UnarchiveTaskView, PersonalTaskDeleteView, PersonalTaskDetailsView
# Team tasks views
from .task_team_views import TeamTaskCreateView, TeamTaskEditView, TeamTaskDeleteView, TasksForApproveView, \
    TeamTaskDetailsView, TaskRejectApproveView

__all__ = [
    # Personal tasks views
    'TaskboardView',
    'PersonalTaskCreateView',
    'ArchivedTasksView',
    'PersonalTaskEditView',
    'UnarchiveTaskView',
    'PersonalTaskDeleteView',
    'PersonalTaskDetailsView',


    # Team tasks views
    'TeamTaskCreateView',
    'TeamTaskEditView',
    'TeamTaskDeleteView',
    'TeamTaskDetailsView',
    'TasksForApproveView',
    'TaskRejectApproveView',
]