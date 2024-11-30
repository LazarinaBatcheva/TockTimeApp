from django.contrib import admin
from tock_time_app.tasks.models import PersonalTask, TeamTask


# Personal tasks
@admin.register(PersonalTask)
class PersonalTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'deadline', 'is_completed', 'created_by']
    list_filter = ['created_by', 'priority', 'is_completed']
    date_hierarchy = 'created_at'
    search_fields = ['created_by',]
    ordering = ['deadline',]


# Teams tasks
@admin.register(TeamTask)
class TeamTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to_username', 'deadline', 'is_completed', 'team']
    list_filter = ['team__name', 'is_completed',]
    date_hierarchy = 'created_at'
    search_fields = ['team', 'assigned_to_username', 'created_by__username']
    ordering = ['deadline',]

    @staticmethod
    def assigned_to_username(obj):
        return ', '.join([member.username for member in obj.team.members.all()])

    assigned_to_username.short_description = 'Assigned To'