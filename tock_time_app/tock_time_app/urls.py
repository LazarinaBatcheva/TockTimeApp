from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tock_time_app.common.urls')),
    path('accounts/', include('tock_time_app.accounts.urls')),
    path('tasks/', include('tock_time_app.tasks.urls')),
    path('teams/', include('tock_time_app.teams.urls')),
]
