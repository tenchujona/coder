from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from business.models import Empresas
from profiles.forms import Edit_Profile_form
from user_register.models import Data_Users
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from business.models import Tag

# Create your views here.

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Edit_Profile_form(request.POST)
            if form.is_valid() and request.POST["password1"]==request.POST["password2"]:
                try:

                   
                    print()
                    UsermodelUpdate = User.objects.get(pk=request.user.id)
                    Data_UsermodelUpdate = Data_Users.objects.get(user_id=request.user.id)
                    Data_UsermodelUpdate.gender = request.POST["genero"]
                    filepath = request.FILES.get('image')
                    password_reset=False

                    if request.POST.getlist('delete') !=[]:
                        UsermodelUpdate.delete()
                        return redirect('home')
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
                    tags = Tag.objects.all()
                    context = {"success": success, "tags":tags}
                    if password_reset:
                        tags = Tag.objects.all()
                        count = range(10)
                        context = {"success": success, "password_reset":password_reset, "count":count, "tags":tags}
                    return render(request, "profile.html", context=context)
                except IntegrityError:
                    exist = True
                    tags = Tag.objects.all()
                    context = {"exist": exist, "tags":tags}
                    return render(request, "profile.html", context=context)
            elif form.cleaned_data["password1"] != form.cleaned_data["password2"]:
                not_match = True
                tags = Tag.objects.all()
                context = {"not_match": not_match, "tags":tags}
                return render(request, "profile.html", context=context)
            else:
                error = True
                tags = Tag.objects.all()
                context = {"error": error, "tags":tags}
                return render(request, "profile.html")
        else:
            tags = Tag.objects.all()
            context = {"tags": tags}
            return render(request, "profile.html", context=context)
    else:
        return redirect('home')

def categori_users(request):
    if request.method == 'POST':
        data = request.POST["user"]
        request.session['data']=data

    users = User.objects.all()
    context = {"usuarios":users}
    return render(request, "all_users.html", context=context)

def profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        print(user.related.gender)
        id = user.id
        bussines_registered = Empresas.objects.get(user_asocied_id=id)
        context = {'usuario':user, 'business':bussines_registered}
        return render(request, "user_profile_view.html", context=context)
    except ObjectDoesNotExist:
        context = {'usuario':user}
        return render(request, "user_profile_view.html", context=context)
