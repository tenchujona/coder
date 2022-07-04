from django import forms

class Edit_Profile_form(forms.Form):
    email = forms.EmailField(max_length=50, required=False)
    password1 = forms.CharField(max_length=70, required=False)
    password2 = forms.CharField(max_length=70, required=False)
    image = forms.ImageField(required=False)
    address = forms.CharField(max_length=100, required=False)
    ocupacion = forms.CharField(max_length=50, required=False)
    numero = forms.CharField(max_length=20, required=False)
    pais = forms.CharField(max_length=20, required=False)
    ciudad = forms.CharField(max_length=20, required=False)