from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import *
from app1.models import *
from app1.models import Data_Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            InsertId= (User.objects.last()).id
            print(InsertId)
            Data_Users.objects.create(user_id =InsertId, birthday = request.POST["birthday"], gender = request.POST["gender"])
            # User.objects.get(pk=InsertId).update(first_name=request.POST["name"])
            UsermodelUpdate= User.objects.get(pk=InsertId)
            UsermodelUpdate.first_name = request.POST["first_name"]
            UsermodelUpdate.last_name = request.POST["last_name"]
            UsermodelUpdate.email = request.POST["email"]
            UsermodelUpdate.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return render(request, "TEMPLATES/index.html")
        else:
            form = UserCreationForm()
            context = {"form":form}
            return render(request, "TEMPLATES/create_users.html", context=context)
    else:
        form = UserCreationForm()
        context = {"form":form}
        return render(request, "TEMPLATES/create_users.html", context=context)

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                context = {"message", f"¡¡Bienvenido {username}!! :)"}
                print(request.user)
                return render(request, "TEMPLATES/index.html")
            else:
                error = True
                form = AuthenticationForm()
                return render(request, "TEMPLATES/login.html", context = error)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {"error":errors, "form":form}
            print(request.user)
            return render(request, "TEMPLATES/login.html", context = context)

    form = AuthenticationForm()
    context = {"form":form}
    return render(request, "TEMPLATES/login.html", context = context)

def search_view(request):
    if request.GET["search"] != (""):
        usuarios_admin = User.objects.filter(username__icontains = request.GET["search"])
        usuarios = Data_Users.objects.filter(
            name__icontains = request.GET["search"],
            username__icontains = request.GET["search"],
            email__icontains = request.GET["search"],
            )
        business = Empresas.objects.filter(
            name__icontains = request.GET["search"], 
            CEO__icontains = request.GET["search"],
            email__icontains = request.GET["search"],
            )
        print(usuarios)
        context = {"usuarios":usuarios, "usuarios_admin":usuarios_admin, "business":business}
        return render(request, "TEMPLATES/search_view.html", context=context)
    else:
        empty = True
        context = {"empty":empty}
        return render(request, "TEMPLATES/index.html", context=context)

def categori_users(request):
    usuarios_admin = User.objects.all()
    usuarios = Data_Users.objects.all()
    context = {"usuarios_admin":usuarios_admin, "usuarios":usuarios}
    return render(request, "TEMPLATES/all_users.html", context=context)

def categori_business(request):
    business = Empresas.objects.all()
    context = {"business":business}
    print(business)
    return render(request, "TEMPLATES/all_business.html", context=context)


def create_business(request):
    if request.method == "GET":
        form = Empresa_form()
        context = {"form":form}
        return render(request, "TEMPLATES/create_business.html", context=context)
    else:
        form = Empresa_form(request.POST)
        if form.is_valid():
            new_product = Empresas.objects.create(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                CEO = form.cleaned_data["CEO"],
                ubicacion = form.cleaned_data["ubicacion"],
                numero = form.cleaned_data["numero"],
            )
            context = {"new_product":new_product}
        return render(request, "TEMPLATES/create_business.html", context=context)
