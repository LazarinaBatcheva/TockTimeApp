from django.db import models


class FriendRequestStatusChoices(models.TextChoices):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    CANCELLED = 'cancelled'