from django.contrib import admin

from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'avatar', 'created_date']
    list_display_links = ['user']
    # list_filter = ['created_date']
    # list_editable = ['first_name', 'last_name']


admin.site.register(Profile, ProfileAdmin)