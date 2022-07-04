from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys

# Create your models here.

class Data_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=20, unique=True, related_name="related")
    image = models.ImageField(upload_to="profile_image", default="default_images/anonymous-user.png")
    gender = models.CharField(
        max_length=9,
        choices=[("Masculino", "Masculino"),("Femenino", "Femenino")]
    )
    birthday = models.DateField()
    category = models.ForeignKey("app1.Category", on_delete=models.CASCADE) # asigana una categoria de la clase categoria
    address = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True, unique=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.user.username

    def save(self):
		#Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (250,250) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Data_Users,self).save()