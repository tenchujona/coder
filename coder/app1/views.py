from multiprocessing import context
from django.db import IntegrityError
from django.shortcuts import redirect, render
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

            try:
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                login(request, user)
                Data_Users.objects.create(user_id =request.user.id,
                    birthday = request.POST["birthday"],
                    gender = request.POST["gender"],
                    category_id = 1)
                UsermodelUpdate = User.objects.get(pk=request.user.id)
                UsermodelUpdate.first_name = request.POST["first_name"]
                UsermodelUpdate.last_name = request.POST["last_name"]
                UsermodelUpdate.email = request.POST["email"]
                UsermodelUpdate.save()
                return render(request, "index.html")
            except:
                User.objects.last().delete()
                error = True
                context = {"error":error}
                return render(request, "create_users.html", context=context)
        elif IntegrityError:
            if request.POST["password1"] != request.POST["password2"]:
                print(form.errors)
                not_match= True
                context = {"not_match":not_match}
                return render(request, "create_users.html", context=context)
            else:
                print(form.errors)
                exist= True
                context = {"exist":exist}
                return render(request, "create_users.html", context=context)
        else:
            print(form.errors)
            error = True
            context = {"error":error}
            return render(request, "create_users.html", context=context)

    form = UserCreationForm()
    context = {"form":form}
    return render(request, "create_users.html", context=context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():

                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')
                
                user = authenticate(username=usuario, password=contra)
                
                if user is not None:
                    login(request, user)
                    context = {"message":f"¡¡Bienvenido {usuario}!! :)"}

                    return render(request, "index.html", context=context)

            else:
                error = True
                context = {"error":error}
                return render(request, "login.html", context = context)
        else:
            return render(request, "login.html")

def search_view(request):
    if request.GET["search"] != (""):

        user = User.objects.filter(username__icontains = request.GET["search"]).select_related("data_users")

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

def categori_users(request):
    users = User.objects.all()

    context = {"usuarios":users}
    return render(request, "all_users.html", context=context)

def categori_business(request):
    business = Empresas.objects.all()
    context = {"business":business}
    return render(request, "all_business.html", context=context)

def create_business(request):
    if request.method == "POST":
        form = Empresa_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                print(request.FILES)
                filepath = request.FILES.get('image') # VERIFICA SI SE ENVIARON ARCHIVOS - SI MultiValueDict CONTIENE EL IMAGE ES VERDAD
                if filepath:
                    new_content = Empresas.objects.create(
                        name = form.cleaned_data["name"],
                        email = form.cleaned_data["email"],
                        CEO = form.cleaned_data["CEO"],
                        ubicacion = form.cleaned_data["ubicacion"],
                        numero = form.cleaned_data["numero"],
                        category_id = 2,
                        image = form.cleaned_data["image"],
                    )
                else:
                    new_content = Empresas.objects.create(
                        name = form.cleaned_data["name"],
                        email = form.cleaned_data["email"],
                        CEO = form.cleaned_data["CEO"],
                        ubicacion = form.cleaned_data["ubicacion"],
                        numero = form.cleaned_data["numero"],
                        category_id = 2,
                    )
                business = Empresas.objects.all()
                context = {"new_content":new_content, "business":business}
                return render(request, "all_business.html", context=context)
            except IntegrityError:
                exists = True
                context = {"exists":exists}
                return render(request, "create_business.html", context=context)
        else:
            print(form.errors)
            error = True
            context = {"error":error}
            return render(request, "create_business.html", context=context)

    form = Empresa_form()
    context = {"form":form}
    return render(request, "create_business.html", context=context)

def profile(request):

    if request.method == "POST":
        form = Edit_form(request.POST)
        if form.is_valid() and request.POST["password1"]==request.POST["password2"]:
            try:
                UsermodelUpdate = User.objects.get(pk=request.user.id)
                Data_UsermodelUpdate = Data_Users.objects.get(user_id=request.user.id)
                Data_UsermodelUpdate.gender = request.POST["genero"]
                filepath = request.FILES.get('image')
                
                if request.POST["username"] != "":
                    UsermodelUpdate.username = request.POST["username"]
                if request.POST["password1"] != "":
                    UsermodelUpdate.set_password(form.cleaned_data['password2'])
                    password_reset = True
                if request.POST["email"] != "":
                    UsermodelUpdate.email = form.cleaned_data["email"]
                if request.POST["first_name"] != "":
                    UsermodelUpdate.first_name = request.POST["first_name"]
                if request.POST["last_name"] != "":
                    UsermodelUpdate.last_name = request.POST["last_name"]
                if request.POST["username"] != "":
                    Data_UsermodelUpdate.address = form.cleaned_data["address"]
                if request.POST["ocupacion"] != "":
                    Data_UsermodelUpdate.ocupacion = form.cleaned_data["ocupacion"]
                if request.POST["numero"] != "":
                    Data_UsermodelUpdate.numero = form.cleaned_data["numero"]
                if request.POST["pais"] != "":
                    Data_UsermodelUpdate.pais = form.cleaned_data["pais"]
                if request.POST["ciudad"] != "":
                    Data_UsermodelUpdate.ciudad = form.cleaned_data["ciudad"]
                if filepath:
                    Data_UsermodelUpdate.image = request.FILES.get("image")
                
                UsermodelUpdate.save()
                Data_UsermodelUpdate.save()
                success = True
                context = {"success": success}
                if password_reset:
                    count = range(10)
                    context = {"success": success, "password_reset":password_reset, "count":count}
                return render(request, "profile.html", context=context)
            except IntegrityError:
                exist = True
                context = {"exist": exist}
                return render(request, "profile.html", context=context)

        elif form.cleaned_data["password1"] != form.cleaned_data["password2"]:
            not_match = True
            context = {"not_match": not_match}
            return render(request, "profile.html", context=context)
        else:
            return render(request, "profile.html")
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')