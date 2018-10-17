from django.contrib import admin

# Register your models here.
from account.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_num')
    list_filter = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)

