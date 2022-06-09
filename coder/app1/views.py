from django.http import HttpResponse
from django.shortcuts import render
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist
from app1.models import Accounts
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        print("primera condicional dentro")
        #user = Accounts.objects.get(username__contains=request.POST["username"])
        #print(request.POST)

        try:
            Accounts.objects.get(username__contains=request.POST["username"], password__contains=request.POST["password"])
            return HttpResponse("sesión iniciada")
        except ObjectDoesNotExist:
            return HttpResponse("usuario y contraseña incorrectos")

    else:
        return render(request, 'TEMPLATES/login.html')

def search_users(request):
    if request.GET["search"] != (""):
        usuarios_admin = User.objects.filter(username__icontains = request.GET["search"])
        usuarios = Accounts.objects.filter(username__icontains = request.GET["search"])
        print(usuarios)
        context = {"usuarios":usuarios, "usuarios_admin":usuarios_admin}
        return render(request, "TEMPLATES/search_users.html", context=context)
    else:
        empty = True
        context = {"empty":empty}
        return render(request, "TEMPLATES/index.html", context=context)

def categori_users(request):
    usuarios_admin = User.objects.all()
    usuarios = Accounts.objects.all()
    context = {"usuarios_admin":usuarios_admin, "usuarios":usuarios}
    return render(request, "TEMPLATES/all_users.html", context=context)

def categori_business(request):
    business = Empresas.objects.all()
    context = {"business":business}
    print(business)
    return render(request, "TEMPLATES/all_business.html", context=context)
