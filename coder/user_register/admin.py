from django.contrib import admin
from user_register.models import Data_Users
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class AccountsInline(admin.StackedInline):
    model = Data_Users
    can_delete = False
    verbose_name_plural = "Usuarios"

class CustomAccountAdmin(UserAdmin):
    inlines = (AccountsInline,)

admin.site.unregister(User)
admin.site.register(User, CustomAccountAdmin)