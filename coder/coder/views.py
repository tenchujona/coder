from django.shortcuts import render
from django.contrib.auth.models import User
from business.models import Empresas

def home(request):
    return render(request, 'index.html')

def search_view(request):
    if request.GET["search"] != (""):

        user = User.objects.filter(username__icontains = request.GET["search"])

        business = Empresas.objects.filter(
            name__icontains = request.GET["search"], 
            CEO__icontains = request.GET["search"],
            email__icontains = request.GET["search"],
            )

        context = {"user":user, "business":business}
        return render(request, "search_view.html", context=context)
    else:
        empty = True
        context = {"empty":empty}
        return render(request, "index.html", context=context)