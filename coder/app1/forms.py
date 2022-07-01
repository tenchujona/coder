import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from pkg_resources import require

class Account_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class Empresa_form(forms.Form):
    name = forms.CharField(max_length=70)
    CEO = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=50)
    ubicacion = forms.CharField(max_length=100)
    numero = forms.CharField()
    image = forms.ImageField(required=False)

class Category_form(forms.Form):
    name = forms.CharField(max_length=30)

class Edit_form(forms.Form):
    email = forms.EmailField(max_length=50, required=False)
    password1 = forms.CharField(max_length=70, required=False)
    password2 = forms.CharField(max_length=70, required=False)
    image = forms.ImageField(required=False)
    address = forms.CharField(max_length=100, required=False)
    ocupacion = forms.CharField(max_length=50, required=False)
    numero = forms.CharField(max_length=20, required=False)
    pais = forms.CharField(max_length=20, required=False)
    ciudad = forms.CharField(max_length=20, required=False)
