from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=9,
        choices=[("Masculino", "Masculino"),("Femenino", "Femenino")]
    )
    birthday = models.DateField()
    def __str__(self) -> str:
        return self.user.username

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
