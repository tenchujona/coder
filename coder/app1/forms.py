from tkinter import W
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Account_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class Empresa_form(forms.Form):
    name = forms.CharField(max_length=70)
    CEO = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=30)
    ubicacion = forms.CharField(max_length=70)
    numero = forms.IntegerField()

class Category_form(forms.Form):
    name = forms.CharField(max_length=30)
