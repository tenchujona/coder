from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys

# Create your models here.

class Data_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=20, unique=True, related_name="related")
    image = models.ImageField(default="default_images/anonymous-user.png", upload_to="profile_image")
    gender = models.CharField(
        max_length=9,
        choices=[("Masculino", "Masculino"),("Femenino", "Femenino")]
    )
    birthday = models.DateField()
    category = models.ForeignKey("business.Category", on_delete=models.CASCADE) # asigana una categoria de la clase categoria
    address = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True, unique=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)

    __original_name = None
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__original_name = self.image

    def __str__(self) -> str:
        return self.user.username

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.image != "default_images/anonymous-user.png" and self.image != self.__original_name:
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