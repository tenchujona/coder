from django import forms


class Account_form(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=30)
    birthday = forms.DateField()
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10)

class Empresa_form(forms.Form):
    name = forms.CharField(max_length=70)
    CEO = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=30)
    ubicacion = forms.CharField(max_length=70)
    numero = forms.IntegerField()

class Category_form(forms.Form):
    name = forms.CharField(max_length=30)
