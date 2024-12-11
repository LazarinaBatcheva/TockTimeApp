from django.db import models


class FriendRequestStatusChoices(models.TextChoices):
    """
    Choices for the status of a friend request.
    Provides predefined options for handling friend request statuses.
    """

    PENDING = 'pending', 'Pending'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'
    CANCELLED = 'cancelled', 'Cancelled'