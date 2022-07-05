from django import forms
from business.models import Tag

class Empresa_form(forms.Form):
    name = forms.CharField(max_length=70)
    CEO = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=50)
    ubicacion = forms.CharField(max_length=100, required=False)
    numero = forms.CharField()
    image = forms.ImageField(required=False)
    biografia = forms.CharField(max_length=350, required=False)
    tags = forms.ModelMultipleChoiceField(required=False, queryset=Tag.objects.all())
    active = forms.BooleanField(required=False)

class Category_form(forms.Form):
    name = forms.CharField(max_length=30)
