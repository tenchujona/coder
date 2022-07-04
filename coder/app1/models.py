from django.db import models
from PIL import Image

# Create your models here.

class Empresas(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=False, null=False)
    CEO = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to="business_image", default="default_images/anonymous-business.png")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="Empresas")
    active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.name+" [Nombre de la Empresa]"

    def save(self, *args, **kwargs): #Redimensiona la imagen
        super().save(*args, **kwargs)  # Guardar la imagen

        img = Image.open(self.image.path) # Abre el archivo usando self

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # Guarda la imagen en el mismo path

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name+" [Categoria]" # añade el nombre a cada categoria creada
