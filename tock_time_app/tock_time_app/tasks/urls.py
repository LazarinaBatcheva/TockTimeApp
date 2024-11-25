from django.urls import path, include
from tock_time_app.tasks import views

personal_task_patterns = [
    path('', views.TaskboardView.as_view(), name='taskboard'),
    path('create/', views.PersonalTaskCreateView.as_view(), name='personal-task-create'),
    path('task/<int:pk>/', include([
        path('', views.PersonalTaskDetailsView.as_view(), name='personal-task-details'),
        path('edit/', views.PersonalTaskEditView.as_view(), name='personal-task-edit'),
        path('delete/', views.PersonalTaskDeleteView.as_view(), name='personal-task-delete'),
    ])),
]

team_task_patterns = [
    path('task/create/', views.TeamTaskCreateView.as_view(), name='team-task-create'),
]

urlpatterns = [
    path('<str:username>/', include([
        path('personal/', include(personal_task_patterns)),
        path('team/<slug:slug>/', include(team_task_patterns)),
    ])),
]
