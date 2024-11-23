from django.urls import path
from tock_time_app.tasks import views

urlpatterns = [
    path('personal/', views.TaskboardView.as_view(), name='taskboard'),
    path('create/', views.CreateTaskView.as_view(), name='task-create'),
]