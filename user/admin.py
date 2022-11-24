from django.contrib import admin
from .models import * 


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'first_name', 'last_name', 'email', 'access_type', 'is_staff','is_active', 'is_superuser']
admin.site.register(CustomUser, CustomUserAdmin)

class UserDetailsAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'gender', 'pin', 'address', 'city', 'district', 'state','country']
admin.site.register(UserDetails, UserDetailsAdmin)