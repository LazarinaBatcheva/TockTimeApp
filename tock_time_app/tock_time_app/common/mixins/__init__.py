"""
Centralized module for importing and re-exporting mixins.

This module aggregates all mixins from various submodules, such as model-related,
form-related, profile access, and queryset mixins. It simplifies imports by
providing a single entry point for all mixins used across the application.
"""

# Model-related mixins
# These mixins add additional fields or behavior to models.
from .model_mixins import (
    DescriptionMixin,
    CreatedAtMixin
)

# Form-related mixins
# These mixins modify form behavior, such as adding placeholders or customizing help text.
from .form_mixins import (
    PlaceholderMixin,
    NoHelpTextMixin,
    MarkRequiredFieldsMixin
)

# Profile access mixins
# These mixins handle access control for user profiles, tasks, and teams.
from .access_mixins import (
    UserProfileAccessMixin,
    UserTaskAccessMixin,
    TeamObjectOwnerAccessMixin,
    ObjectCreatorMixin
)

# Queryset mixins
# These mixins provide queryset-related functionality for filtering data.
from .queryset_mixins import (
    UserTeamsMixin,
    UserTasksMixin
)

__all__ = [
    # Model-related mixins
    'DescriptionMixin',
    'CreatedAtMixin',

    # Form-related mixins
    'PlaceholderMixin',
    'NoHelpTextMixin',
    'MarkRequiredFieldsMixin',

    # Profile access mixins
    'UserProfileAccessMixin',
    'UserTaskAccessMixin',
    'TeamObjectOwnerAccessMixin',
    'ObjectCreatorMixin',

    # Queryset mixins
    'UserTeamsMixin',
    'UserTasksMixin',
]