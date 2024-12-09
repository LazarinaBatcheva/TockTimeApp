from django.urls import path, include
from tock_time_app.tasks import views

personal_task_patterns = [
    path('', views.TaskboardView.as_view(), name='personal-taskboard'),
    path('create/', views.PersonalTaskCreateView.as_view(), name='personal-task-create'),
    path('archived/', include([
        path('', views.ArchivedTasksView.as_view(), name='personal-tasks-archive'),
        path('<int:pk>/unarchive/', views.UnarchiveTaskView.as_view(), name='personal-task-unarchive')
    ])),
    path('task/<int:pk>/', include([
        path('', views.PersonalTaskDetailsView.as_view(), name='personal-task-details'),
        path('edit/', views.PersonalTaskEditView.as_view(), name='personal-task-edit'),
        path('delete/', views.PersonalTaskDeleteView.as_view(), name='personal-task-delete'),
    ])),
]

team_task_patterns = [
    path('task/create/', views.TeamTaskCreateView.as_view(), name='team-task-create'),
    path('task/<int:pk>/', include([
        path('', views.TeamTaskDetailsView.as_view(), name='team-task-details'),
        path('edit/', views.TeamTaskEditView.as_view(), name='team-task-edit'),
        path('delete/', views.TeamTaskDeleteView.as_view(), name='team-task-delete'),
    ])),
    path('tasks-for-approve/', include([
        path('', views.TasksForApproveView.as_view(), name='tasks-for-approve'),
        path('task/<int:pk>/', views.TaskRejectApproveView.as_view(), name='task-reject-approve'),
    ])),
]

urlpatterns = [
    path('<str:username>/', include([
        path('personal/', include(personal_task_patterns)),
        path('team/<slug:slug>/', include(team_task_patterns)),
    ])),
]
