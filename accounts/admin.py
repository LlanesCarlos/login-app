from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
            )}
         ),
    )
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'age',
            'password'
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
    )
    search_fields = ('username', 'email')    # postscript

admin.site.register(CustomUser, UserAdmin)