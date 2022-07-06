from django.shortcuts import render
from django.contrib.auth.models import User
from business.models import Empresas, Tag
from business.models import About

def home(request):
    tags = Tag.objects.all()
    context = {"tags":tags}
    return render(request, 'index.html', context=context)

def search_view(request):
    if request.GET["search"] != (""):

        user = User.objects.filter(username__icontains = request.GET["search"])

        business = Empresas.objects.filter(
            name__icontains = request.GET["search"],
            )
        tags = Tag.objects.all()
        context = {"user":user, "business":business, "tags":tags}
        return render(request, "search_view.html", context=context)
    else:
        empty = True
        tags = Tag.objects.all()
        context = {"empty":empty, "tags":tags}
        return render(request, "index.html", context=context)

def about(request):
    tags = Tag.objects.all()
    img = About.objects.all()
    print(img)
    context = {"tags":tags, "img":img}
    return render(request, "about.html", context=context)
