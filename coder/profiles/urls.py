from django.urls import path

from profiles.views import edit_profile, categori_users

urlpatterns = [
    path('my-profile/', edit_profile, name="login"),
    path('all-users/', categori_users, name="mostrar usuarios"),
]