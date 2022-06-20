"""coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from coder.views import home
from app1.views import *

from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login', login_view, name="login"),
    path('buscar/', search_view, name="login"),
    path('all-users/', categori_users, name="login"),
    path('all-business/', categori_business, name="login"),
    path('create-business/', create_business, name="login"),
    path('create-user', create_user, name="login"),
    path('logout', LogoutView.as_view(template_name="TEMPLATES/index.html"), name="logout"),
]

#IMAGES
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
