from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

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
                    return redirect("home")

            else:
                error = True
                context = {"error":error}
                return render(request, "login.html", context = context)
        else:
            return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')