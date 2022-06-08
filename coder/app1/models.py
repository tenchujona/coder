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