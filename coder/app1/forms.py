from django import forms

class Empresa_form(forms.Form):
    name = forms.CharField(max_length=70)
    CEO = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=50)
    ubicacion = forms.CharField(max_length=100)
    numero = forms.CharField()
    image = forms.ImageField(required=False)

class Category_form(forms.Form):
    name = forms.CharField(max_length=30)
