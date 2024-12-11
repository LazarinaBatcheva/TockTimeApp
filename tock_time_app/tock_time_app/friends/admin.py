from django.contrib import admin
from tock_time_app.friends.models import FriendRequest


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for FriendRequest model.
    Provides a list view, filters and search functionality.
    """

    list_display = ['sender', 'receiver', 'status', 'created_at']
    list_filter = ['status',]
    search_fields = ['sender__username', 'receiver__username']
    date_hierarchy = 'created_at'
    ordering = ['created_at',]

    # Organize fields in the edit form
    fieldsets = (
        (None, {
            'fields': ('sender', 'receiver', 'status'),
        }),
        ('Additional Info', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # Collapse this section for better UI
        }),
    )
    readonly_fields = ('created_at',)   # Prevent manual editing of `created_at`