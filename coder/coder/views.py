from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from business.models import Empresas, Tag
from django.template import Template, Context

def home(request):
    tags = Tag.objects.all()
    context = {"tags":tags}
    return render(request, 'index.html', context=context)

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