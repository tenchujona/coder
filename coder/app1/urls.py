from django.urls import path

from app1.views import *

urlpatterns = [
    path('login', login_view, name="login"),
    path('buscar/', search_view, name="login"),
    path('all-users/', categori_users, name="login"),
    path('all-business/', categori_business, name="login"),
    path('create-business/', create_business, name="login"),
    path('signup', create_user, name="login"),
    path('logout', logout_view, name="logout"),
    path('my-profile/', profile, name="mi perfil"),
]