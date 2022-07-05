from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from user_register.models import Data_Users
from django.contrib.auth.models import User
from django.db import IntegrityError
from business.models import Tag

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():

            try:
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                login(request, user)
                UsermodelUpdate = User.objects.get(pk=request.user.id)
                UsermodelUpdate.first_name = request.POST["first_name"]
                UsermodelUpdate.last_name = request.POST["last_name"]
                UsermodelUpdate.email = request.POST["email"]
                UsermodelUpdate.save()
                Data_Users.objects.create(
                    user_id = request.user.id,
                    birthday = request.POST["birthday"],
                    gender = request.POST["gender"],
                    category_id = 1)
                return render(request, "index.html")
            except:
                User.objects.last().delete()
                error = True
                tags = Tag.objects.all()
                context = {"error":error, "tags":tags}
                return render(request, "create_users.html", context=context)
        elif IntegrityError:
            if request.POST["password1"] != request.POST["password2"]:
                print(form.errors)
                not_match= True
                tags = Tag.objects.all()
                context = {"not_match":not_match, "tags":tags}
                return render(request, "create_users.html", context=context)
            else:
                print(form.errors)
                exist= True
                tags = Tag.objects.all()
                context = {"exist":exist, "tags":tags}
                return render(request, "create_users.html", context=context)
        else:
            print(form.errors)
            error = True
            tags = Tag.objects.all()
            context = {"error":error, "tags":tags}
            return render(request, "create_users.html", context=context)

    form = UserCreationForm()
    tags = Tag.objects.all()
    context = {"form":form, "tags":tags}
    return render(request, "create_users.html", context=context)