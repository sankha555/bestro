from django.db import models
from PIL import Image

from items.constants import CATEGORIES

class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField(max_length=500)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    is_non_veg = models.BooleanField(default=False)    
    stock = models.IntegerField(default=10)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5)
    image = models.ImageField(verbose_name="Feature Image", upload_to="item_pics", default="media/default_item.png")
    #non_availablity_time = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    
class Combo(models.Model):
    name = models.CharField(max_length=50, default = "")
    description = models.TextField(max_length=500, default="")
    item1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item1")
    item2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item2")    
    item3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item3")    
    item4 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item4")    
    item5 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item5")    
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5)
    image = models.ImageField(verbose_name="Feature Image", upload_to="item_pics", default="media/default_item.png")
    non_availablity_time = models.DateTimeField(auto_now=False, null=True)
    
    def save(self, *args, **kwargs):
        calculate_rate(self)
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def calculate_rate(self):
        self.rate = 0
        if self.item1:
            self.rate += item1.rate
        if self.item2:
            self.rate += item2.rate
        if self.item3:
            self.rate += item3.rate
        if self.item4:
            self.rate += item4.rate
        if self.item5:
            self.rate += item5.rate
            
    @property
    def is_available(self):
        if item1 is not None and item1.stock == 0:
            return False
        if item2 is not None and item2.stock == 0:
            return False
        if item3 is not None and item3.stock == 0:
            return False
        if item4 is not None and item4.stock == 0:
            return False
        if item5 is not None and item5.stock == 0:
            return False
        
        return True

# Create your models here.
