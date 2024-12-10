from django.contrib import admin
from tock_time_app.friends.models import FriendRequest


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('sender__username', 'receiver__username')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)

