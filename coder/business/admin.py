from django.contrib import admin
from business.models import *

# Register your models here.

# class AvatarInline(admin.StackedInline):
#     model= Avatar
#     can_delete = False
#     verbose_name_plural = "Foto de perfil"

admin.site.register(Empresas)
admin.site.register(Category)
# admin.site.register(Avatar)