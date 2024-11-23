from django.urls import path, include
from tock_time_app.teams import views

teams_patterns = [
    path('', views.TeamsDashboardView.as_view(), name='teams-dashboard'),
    path('create/', views.TeamCreateView.as_view(), name='team-create'),
]

urlpatterns = [
    path('<str:username>/teams/', include(teams_patterns))
]