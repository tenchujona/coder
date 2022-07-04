from django.urls import path

from app1.views import *

urlpatterns = [
    path('all-business/', categori_business, name="mostrar empresas"),
    path('create-business/', create_business, name="crear una empresa"),
]