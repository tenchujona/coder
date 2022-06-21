from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app1.forms import *
from app1.models import *
from app1.models import Data_Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            try:
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                InsertId= (User.objects.last()).id
                Data_Users.objects.create(user_id =InsertId, birthday = request.POST["birthday"], gender = request.POST["gender"], category_id = 1)
                UsermodelUpdate= User.objects.get(pk=InsertId)
                UsermodelUpdate.first_name = request.POST["first_name"]
                UsermodelUpdate.last_name = request.POST["last_name"]
                UsermodelUpdate.email = request.POST["email"]
                UsermodelUpdate.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                
                return render(request, "TEMPLATES/index.html")
            except:
                User.objects.last().delete()
                error = True
                context = {"error":error}
                return render(request, "TEMPLATES/create_users.html", context=context)
        elif IntegrityError:
            print("OK.")
            exist= True
            context = {"exist":exist}
            return render(request, "TEMPLATES/create_users.html", context=context)
        else:
            error = True
            context = {"error":error}
            return render(request, "TEMPLATES/create_users.html", context=context)

    form = UserCreationForm()
    context = {"form":form}
    return render(request, "TEMPLATES/create_users.html", context=context)

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password"]
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                context = {"message":f"¡¡Bienvenido {usuario}!! :)"}

                return render(request, "TEMPLATES/index.html", context=context)
            else:
                form = AuthenticationForm()
                context = {"message", f"¡¡Bienvenido {usuario}!! :)"}
                return render(request, "TEMPLATES/login.html", context=context)
        else:

            form = AuthenticationForm()
            context = {"form":form}
            return render(request, "TEMPLATES/login.html", context = context)
    else:

        form = AuthenticationForm()
        context = {"form":form}
        return render(request, "TEMPLATES/login.html", context = context)

def search_view(request):
    if request.GET["search"] != (""):

        user = User.objects.filter(username__icontains = request.GET["search"]).select_related("data_users")

        business = Empresas.objects.filter(
            name__icontains = request.GET["search"], 
            CEO__icontains = request.GET["search"],
            email__icontains = request.GET["search"],
            )

        context = {"user":user, "business":business}
        return render(request, "TEMPLATES/search_view.html", context=context)
    else:
        empty = True
        context = {"empty":empty}
        return render(request, "TEMPLATES/index.html", context=context)

def categori_users(request):
    users = User.objects.all().select_related("data_users")
    context = {"usuarios":users}
    return render(request, "TEMPLATES/all_users.html", context=context)

def categori_business(request):
    business = Empresas.objects.all()
    context = {"business":business}
    return render(request, "TEMPLATES/all_business.html", context=context)


def create_business(request):
    if request.method == "POST":
        form = Empresa_form(request.POST)
        if form.is_valid():
            try:
                new_content = Empresas.objects.create(
                    name = form.cleaned_data["name"],
                    email = form.cleaned_data["email"],
                    CEO = form.cleaned_data["CEO"],
                    ubicacion = form.cleaned_data["ubicacion"],
                    numero = form.cleaned_data["numero"],
                    category_id = 2,
                )
                new = True
                business = Empresas.objects.all()
                context = {"new_content":new_content, "business":business, "new":new}
                print(new_content)
                return render(request, "TEMPLATES/all_business.html", context=context)
            except IntegrityError:
                exists = True
                context = {"exists":exists}
                return render(request, "TEMPLATES/create_business.html", context=context)
        else:
            error = True
            context = {"error":error}
            return render(request, "TEMPLATES/create_business.html", context=context)

    form = Empresa_form()
    context = {"form":form}
    return render(request, "TEMPLATES/create_business.html", context=context)
