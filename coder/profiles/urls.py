from django.urls import path, re_path

from profiles.views import edit_profile, categori_users, profile_view

urlpatterns = [
    path('my-profile/', edit_profile, name="login"),
    path('all-users/', categori_users, name="mostrar usuarios"),
    re_path(r'^profile/(?P<username>\w{0,50})/$', profile_view, name="mostrar perfil de usuario"),
]