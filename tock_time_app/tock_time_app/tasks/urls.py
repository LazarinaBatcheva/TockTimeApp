from django.urls import path, include
from tock_time_app.tasks import views

personal_task_patterns = [
    path('', views.TaskboardView.as_view(), name='taskboard'),
    path('create/', views.CreateTaskView.as_view(), name='task-create'),
    path('task/<int:pk>/', include([
        path('', views.TaskDetailsView.as_view(), name='task-details'),
        path('edit/', views.TaskEditView.as_view(), name='task-edit'),
        path('delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    ])),
]

urlpatterns = [
    path('<str:username>/personal/', include(personal_task_patterns)),
]
