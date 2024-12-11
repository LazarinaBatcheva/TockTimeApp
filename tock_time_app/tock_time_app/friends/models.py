"""
Model for managing friend requests in the friends app.

This model defines the relationship between users sending and receiving friend requests,
along with the status and timestamps.
"""

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint

from tock_time_app.friends.choices import FriendRequestStatusChoices

UserModel = get_user_model()


class FriendRequest(models.Model):
    """ Represents a friend request between two users. """

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

    def clean(self):
        """
        Ensures that the sender and receiver are not the same user.

        Raises:
            ValidationError: If the sender and receiver are the same user.
        """
        if self.sender == self.receiver:
            raise ValidationError("You cannot send a friend request to yourself.")

    def __str__(self):
        return f'{self.sender} -> {self.receiver} ({self.status})'

    class Meta:
        constraints = [
            UniqueConstraint(fields=['sender', 'receiver'], name='unique_friend_request')
        ]
        ordering = ['-created_at']