from django.urls import path, include
from tock_time_app.teams import views

urlpatterns = [
    path('<str:username>/team/', include([
        path('', views.TeamsDashboardView.as_view(), name='teams-dashboard'),
        path('create/', views.TeamCreateView.as_view(), name='team-create'),
        path('<slug:slug>/', include([
            path('', views.TeamDetailsView.as_view(), name='team-details'),
            path('edit/', views.TeamEditView.as_view(), name='team-edit'),
            path('delete/', views.TeamDeleteView.as_view(), name='team-delete'),
        ])),
    ]))
]