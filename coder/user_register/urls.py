from django.urls import path

from user_register.views import register

urlpatterns = [
    path('signup/', register, name="registrarse"),
]