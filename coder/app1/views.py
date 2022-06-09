from django.http import HttpResponse
from django.shortcuts import render
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist
from app1.models import Accounts

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
    usuarios = Accounts.objects.filter(username__icontains = request.GET["search"])
    print(usuarios)
    context = {"usuarios":usuarios}
    return render(request, "TEMPLATES/search_users.html", context=context)
