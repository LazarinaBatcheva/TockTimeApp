from django.contrib import admin

from tock_time_app.teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Team model.
    Provides functionality for managing teams in the admin panel.
    """

    list_display = ['name', 'created_by', 'get_members_names', 'created_at']
    search_fields = ['name', 'members__username']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['name',]
    readonly_fields = ['created_at',]

    fieldsets = (
        (None, {
            'fields': ('name', 'members')
        }),
        ('Details', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ['members']

    @staticmethod
    def get_members_names(obj):
        """ Custom method to display member usernames in the list view. """

        return ', '.join([member.username for member in obj.members.all()])
