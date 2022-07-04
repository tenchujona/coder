from django.urls import path

from login.views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]