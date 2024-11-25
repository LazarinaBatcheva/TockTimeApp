import re
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


def camel_to_snake(name):
    """
    Converts CamelCase to snake_case.
    Example: TeamTask -> team_task
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


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


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name=None,
    )

    class Meta:
        abstract = True

    def contribute_to_class(self, cls, name):
        super().contribute_to_class(cls, name)

        field = cls._meta.get_field('created_by')
        field.remote_field.related_name = f'created_{camel_to_snake(cls.__name__)}s'