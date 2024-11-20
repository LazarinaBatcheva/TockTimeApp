from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from tock_time_app.accounts.forms import AppUserCreationForm, AppUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ['username', 'email', 'is_staff', 'is_superuser']
    readonly_fields = ['date_joined', ]
    search_fields = ['username', 'email']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', )}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )

    search_help_text = 'Use the search bar to find users by username or email.'
    actions = ['deactivate_users', 'activate_users', 'make_staff', 'revoke_staff']
    actions_selection_counter = 'selected users'

    @admin.action(description='Deactivate selected app users')
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description='Activate selected app users')
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Make selected app users staff')
    def make_staff(self, request, queryset):
        queryset.update(is_staff=True)

    @admin.action(description='Revoke staff status from selected app users')
    def revoke_staff(self, request, queryset):
        queryset.update(is_staff=False)
