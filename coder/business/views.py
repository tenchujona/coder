from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from requests import request
from business.forms import *
from business.models import Empresas, Tag
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

def categori_business(request):
    business = Empresas.objects.all()
    tags = Tag.objects.all()
    context = {"business":business, "tags":tags}
    return render(request, "all_business.html", context=context)

def create_business(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Empresa_form(data=request.POST, files=request.FILES)
            print(form)
            if form.is_valid():
                try:
                    print(request.user.id)
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
                            user_asocied_id = request.user.id,
                        )
                    else:
                        new_content = Empresas.objects.create(
                            name = form.cleaned_data["name"],
                            email = form.cleaned_data["email"],
                            CEO = form.cleaned_data["CEO"],
                            ubicacion = form.cleaned_data["ubicacion"],
                            numero = form.cleaned_data["numero"],
                            category_id = 2,
                            user_asocied_id = request.user.id,
                        )
                    business = Empresas.objects.all()
                    tags = Tag.objects.all()
                    context = {"new_content":new_content, "business":business, "tags":tags}
                    return render(request, "all_business.html", context=context)
                except IntegrityError:
                    exists = True
                    tags = Tag.objects.all()
                    context = {"exists":exists, "tags":tags}
                    return render(request, "create_business.html", context=context)
            else:
                print(form.errors)
                error = True
                tags = Tag.objects.all()
                context = {"error":error, "tags":tags}
                return render(request, "create_business.html", context=context)

        form = Empresa_form()
        tags = Tag.objects.all()
        context = {"form":form, "tags":tags}
        return render(request, "create_business.html", context=context)
    else:
        return redirect('home')

def business_profile_view(request, empresa):

    business = Empresas.objects.get(name=empresa)
    user_id = business.user_asocied_id
    user = User.objects.get(pk=user_id)
    tag = Tag.objects.filter(tag_category=business.id)
    tags = Tag.objects.all()

    context = {'empresa':business, 'user':user, 'tags_profile':tag, 'tags':tags}
    return render(request, "business_profile_view.html", context=context)

def edit_business(request):
    try:
        if request.method == 'POST':
            form = Empresa_form(data=request.POST)
            
            if form.is_valid():
                BusinessUpdate = Empresas.objects.get(user_asocied_id=request.user.id)
                filepath = request.FILES.get('image')

                if request.POST["name"] != "":
                    BusinessUpdate.name = form.cleaned_data["name"]
                if request.POST["biografia"] != "":
                    BusinessUpdate.biografia = form.cleaned_data["biografia"]
                if request.POST["CEO"] != "":
                    BusinessUpdate.CEO = form.cleaned_data["CEO"]
                if request.POST["email"] != "":
                    BusinessUpdate.email = form.cleaned_data["email"]
                if request.POST["numero"] != "":
                    BusinessUpdate.numero = form.cleaned_data["numero"]
                if request.POST["ubicacion"] != "":
                    BusinessUpdate.ubicacion = form.cleaned_data["ubicacion"]
                if request.POST["estado"] == "Activo":
                    BusinessUpdate.active = True
                if request.POST["estado"] != "Activo":
                    BusinessUpdate.active = False
                if request.POST["tags"] != None:
                    BusinessUpdate.tag.set(request.POST.getlist('tags'))
                if filepath and BusinessUpdate.image != request.FILES.get("image"):
                    print('CAMBIO DE IMAGEN')
                    print(BusinessUpdate.image)
                    BusinessUpdate.image = request.FILES.get("image")

                BusinessUpdate.save()
                business = Empresas.objects.get(user_asocied_id=request.user.id)
                tags = Tag.objects.all()
                success = True
                context = {"success": success, 'business':business, 'tags':tags}
                return redirect('crear una empresa')
            else:
                print(form.errors)
                error = True
                context = {"error": error}
                return render(request, 'business.html', context=context)
        else:
            business = Empresas.objects.get(user_asocied_id=request.user.id)
            tags = Tag.objects.all()
            context = {'empresa': business, 'tags': tags}
            return render(request, 'business.html', context=context)
    except ObjectDoesNotExist:
        not_exist = True
        context = {"not_exist": not_exist}
        return render(request, 'business.html', context=context)

def categoryview(request, cats):
    tag_obj = get_object_or_404(Tag, pk=Tag.objects.get(name=cats).id)
    business = Empresas.objects.filter(tag=tag_obj)
    tags = Tag.objects.all()
    context = {'business':business, 'tags':tags}
    return render(request, 'category.html', context)
