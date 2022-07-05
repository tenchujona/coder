from django.db import IntegrityError
from django.shortcuts import redirect, render
from business.forms import *
from business.models import Empresas
from django.contrib.auth.models import User

# Create your views here.

def categori_business(request):
    business = Empresas.objects.all()
    context = {"business":business}
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
    else:
        return redirect('home')

def business_profile_view(request, empresa):

    business = Empresas.objects.get(name=empresa)
    user_id = business.user_asocied_id
    user = User.objects.get(pk=user_id)
    print(business.ubicacion)
    context = {'empresa':business, 'user':user}
    return render(request, "business_profile_view.html", context=context)
