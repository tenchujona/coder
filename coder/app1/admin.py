from django.contrib import admin
from app1.models import *
from django.contrib.auth.models import User, BaseUserManager
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountsInline(admin.StackedInline):
    model = Data_Users
    can_delete = False
    verbose_name_plural = "Usuarios"

# class AvatarInline(admin.StackedInline):
#     model= Avatar
#     can_delete = False
#     verbose_name_plural = "Foto de perfil"

class CustomAccountAdmin(UserAdmin):
    inlines = (AccountsInline,)

admin.site.unregister(User)
admin.site.register(User, CustomAccountAdmin)

admin.site.register(Empresas)
admin.site.register(Category)
# admin.site.register(Avatar)