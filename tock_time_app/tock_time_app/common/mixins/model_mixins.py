import re
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class DescriptionMixin(models.Model):
    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        abstract = True
