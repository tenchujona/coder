from tabnanny import verbose
from django.db import models

# Create your models here.

class Accounts(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.DateField()
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Empresas(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, null=False)
    CEO = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    ubicacion = models.CharField(max_length=70)
    numero = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
