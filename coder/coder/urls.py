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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from coder.views import home, search_view
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('business/', include("app1.urls"), name="extends url"),
    path('buscar/', search_view, name="buscar"),
    path('accounts/', include('user_register.urls'), name="extends url"),
    path('accounts/', include('login.urls'), name="extends url"),
    path('accounts/', include('profiles.urls'), name="extends url"),
]

#IMAGES
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
