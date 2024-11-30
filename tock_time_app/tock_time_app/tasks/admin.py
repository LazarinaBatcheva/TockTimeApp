from django.contrib import admin
from tock_time_app.tasks.models import PersonalTask, TeamTask


# Personal tasks
@admin.register(PersonalTask)
class PersonalTaskAdmin(admin.ModelAdmin):
    """ Admin configuration for managing personal tasks in the admin panel. """

    list_display = ['title', 'priority', 'deadline', 'is_completed', 'created_by']
    list_filter = ['created_by', 'priority', 'is_completed']
    date_hierarchy = 'created_at'
    search_fields = ['created_by',]
    ordering = ['deadline',]


# Teams tasks
@admin.register(TeamTask)
class TeamTaskAdmin(admin.ModelAdmin):
    """ Admin configuration for managing team tasks in the admin panel. """

    list_display = ['title', 'assigned_to_username', 'deadline', 'is_completed', 'team']
    list_filter = ['team__name', 'is_completed',]
    date_hierarchy = 'created_at'
    search_fields = ['team', 'assigned_to_username', 'created_by__username']
    ordering = ['deadline',]

    @staticmethod
    def assigned_to_username(obj):
        """ Custom method to display usernames of users assigned to the task in the list view. """

        return ', '.join([member.username for member in obj.team.members.all()])