"""
Main URL configuration for the project.

This module defines the root URL patterns for the project, including:
- Django admin panel
- Core app routes (common, accounts, tasks, teams, friends)
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),
    # Common application routes
    path('', include('tock_time_app.common.urls')),
    # User accounts (authentication and profiles)
    path('accounts/', include('tock_time_app.accounts.urls')),
    # Task management
    path('tasks/', include('tock_time_app.tasks.urls')),
    # Team management
    path('teams/', include('tock_time_app.teams.urls')),
    # Friendships and REST API
    path('friends/', include('tock_time_app.friends.urls')),
]
