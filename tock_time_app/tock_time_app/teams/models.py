from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from tock_time_app.common.mixins import DescriptionMixin, CreatedAtMixin

UserModel = get_user_model()


class Team(DescriptionMixin, CreatedAtMixin, models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='created_teams',
    )

    members = models.ManyToManyField(
        to=UserModel,
        related_name='teams',
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
