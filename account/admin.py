from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        # (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', "last_name", 'email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Others', {'fields': (
                'service', 'msisdn', 'channel', 'status', 'first_reg_time', 'last_reg_time', 'last_unreg_time',
                'last_renew_time', 'last_reply_time', 'effective_time', 'expiry_time'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
