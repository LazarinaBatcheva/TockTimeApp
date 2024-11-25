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

urlpatterns = [
    path('<str:username>/personal/', include(personal_task_patterns)),
]
