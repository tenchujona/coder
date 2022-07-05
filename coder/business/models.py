import sys
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# Create your models here.

class Empresas(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, null=False)
    CEO = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to="business_image", default="default_images/anonymous-business.png")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="Empresas")
    user_asocied=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_asocied")
    active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.name+" [Nombre de la Empresa]"

    def save(self, *args, **kwargs):
        if self.image != "default_images/anonymous-user.png":
            print(self.image,"<-- IMAGEN NAME")
            #Abre el archivo
            im = Image.open(self.image)

            output = BytesIO()

            #Modifica el archivo para redimencionarlo
            im = im.resize( (250,250) )

            #Guarda el archivo
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            #Cambia el campo del archivo por el nuevo archivo modificado
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            super(Empresas,self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name+" [Categoria]" # añade el nombre a cada categoria creada
