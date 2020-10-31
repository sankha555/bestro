from django.db import models
from django.contrib.auth.models import User

from users.constants import DESIGNATIONS

from PIL import Image

class Customer(models.Model):
    """
    Details of each customer registered on the website are stored as
    an instance of the Customer class. The relevant fields are enumerated below.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="", blank=False, null=False)
    address = models.TextField(max_length=1000, default="", blank=False, null=False)
    phone = models.CharField(verbose_name = "Mobile", max_length=14)
    email = models.EmailField(max_length=254)
    
    image = models.ImageField(verbose_name="Profile Picture", upload_to="customer_pics", default="media/default_user.png")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
            
class Staff(models.Model):
    """
    Details of the each staff of the website are stored as
    an instance of the Staff class. The relevant fields are enumerated below.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(verbose_name="Employee ID", max_length=50)
    name = models.CharField(max_length=100, default="", blank=False, null=False)
    #designation = models.CharField(choices=DESIGNATIONS, max_length=50)
    phone = models.CharField(verbose_name = "Mobile", max_length=14)
    email = models.EmailField(max_length=254)
    
    image = models.ImageField(verbose_name="Profile Picture", upload_to="customer_pics", default="media/default_user.png")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

# Create your models here.
