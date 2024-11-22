# AppUser views
from .app_user_views import AppUserRegisterView, AppUserLogInView, AppUserLogOutView

# Profile views
from .app_profile_views import ProfileEditView, ProfileDeleteView, ProfileDeletedPageView, ProfileDetailsView


__all__ = [
    'AppUserRegisterView',
    'AppUserLogInView',
    'AppUserLogOutView',
    'ProfileEditView',
    'ProfileDeleteView',
    'ProfileDeletedPageView',
    'ProfileDetailsView',
]