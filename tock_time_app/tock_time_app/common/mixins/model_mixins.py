import re
from django.contrib.auth import get_user_model
from django.db import models

# Get the currently active user model
UserModel = get_user_model()


class DescriptionMixin(models.Model):
    """ Adds an optional description field to the model. """

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    """ Adds a created_at field to store the creation timestamp of the model instance. """

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        abstract = True
