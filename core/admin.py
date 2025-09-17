from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('User Bio-data', {
            "classes": ('wide',),
            "fields": (
                'username', 'password1', 'password2',
                'first_name', 'last_name', 'email',
                'is_active', 'is_staff',
                'state', 'city', 'address', 'phone',
            ),
        }),
    )

    fieldsets=UserAdmin.fieldsets + (
        ("Bio",{"fields":('state','city','address','phone')}),
    ) 

admin.site.register(CustomUser,CustomUserAdmin)
