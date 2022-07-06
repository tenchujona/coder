from audioop import reverse
from enum import unique
import sys
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# Create your models here.

class About(models.Model):
    img = models.ImageField(upload_to="default_images", default="default_images/pagina-web.jpg")

    def __str__(self) -> str:
        return 'Imagen para la rout about'

    class Meta:
        verbose_name = "Imagen para la rout about"

class Empresas(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, null=False)
    CEO = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to="business_image", default="default_images/anonymous-business.png")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category", null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name="tag_category")
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    user_asocied=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_asocied")
    biografia=models.CharField(max_length=350, blank=True, null=True)
    active = models.BooleanField(default=True, null=True)

    __original_name = None

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__original_name = self.image

    def __str__(self) -> str:
        return self.name+" [Nombre de la Empresa]"
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.image != "default_images/anonymous-business.png" and self.image != self.__original_name:
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

            super().save(force_insert, force_update, *args, **kwargs)
        else:
            super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name # añade el nombre a cada categoria creada

class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name # añade el nombre
