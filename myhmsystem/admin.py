from django.contrib import admin
from myhmsystem.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# class AccountAdmin(UserAdmin):
#     list_display = ("email", "username", "date_joined",
#                     'last_login', 'is_admin', 'is_staff')
#     search_fields = ('email', 'username')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register( AccountAdmin)
# admin.site.register(Appointment)
admin.site.register(User)
admin.site.register(Responses)
admin.site.register(Appointment)
