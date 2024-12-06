from django.contrib.auth import get_user_model
from django.db import models
from tock_time_app.friends.choices import FriendRequestStatusChoices

UserModel = get_user_model()


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='send_friend_requests',
    )

    receiver = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='received_friend_requests',
    )

    status = models.CharField(
        max_length=20,
        choices=FriendRequestStatusChoices.choices,
        default=FriendRequestStatusChoices.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.sender} -> {self.receiver} ({self.status})'

    class Meta:
        unique_together = ('sender', 'receiver')