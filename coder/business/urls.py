from django.urls import path, re_path

from business.views import *

urlpatterns = [
    path('all-business/', categori_business, name="mostrar empresas"),
    path('create-business/', create_business, name="crear una empresa"),
    path('edit-business/', edit_business, name="editar mi empresa"),
    re_path(r'^business-profile/(?P<empresa>[\w|\W]+)/$', business_profile_view, name="mostrar perfil de emmpresa"),
    path(r'category/<str:cats>/', categoryview, name="categoria"),
]