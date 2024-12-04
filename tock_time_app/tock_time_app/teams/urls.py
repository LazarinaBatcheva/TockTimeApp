from django.urls import path, include
from tock_time_app.teams import views

teams_patterns = [
    path('', views.TeamsDashboardView.as_view(), name='teams-dashboard'),
    path('create/', views.TeamCreateView.as_view(), name='team-create'),
    path('<slug:slug>/', include([
        path('', views.TeamDetailsView.as_view(), name='team-details'),
        path('edit/', views.TeamEditView.as_view(), name='team-edit'),
    ])),
]

urlpatterns = [
    path('<str:username>/team/', include(teams_patterns))
]