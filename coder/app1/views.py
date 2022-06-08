from django.http import HttpResponse
from django.shortcuts import render
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist

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
