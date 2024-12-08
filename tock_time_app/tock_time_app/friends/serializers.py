from rest_framework import serializers
from tock_time_app.friends.models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = ['id', 'sender_username', 'receiver', 'status', 'created_at']
        read_only_fields = ['id', 'sender_username', 'created_at']

    def get_sender_username(self, obj):
        return obj.sender.username if obj.sender else None