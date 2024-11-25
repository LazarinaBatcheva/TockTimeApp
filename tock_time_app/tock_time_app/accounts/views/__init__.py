# AppUser views
from .app_user_views import AppUserRegisterView, AppUserLogInView, AppUserLogOutView
# Profile views
from .app_profile_views import ProfileEditView, ProfileDeleteView, ProfileDeletedPageView, ProfileDetailsView


__all__ = [
    # AppUser views
    'AppUserRegisterView',
    'AppUserLogInView',
    'AppUserLogOutView',

    # Profile views
    'ProfileEditView',
    'ProfileDeleteView',
    'ProfileDeletedPageView',
    'ProfileDetailsView',
]