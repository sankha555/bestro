from django.db import models
from django_mysql.models import JSONField, Model
from django.utils import timezone
from datetime import datetime, date

from users.models import Customer
from items.models import Item, Combo

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_placed = models.DateTimeField(default=date.today())
    time_placed = models.TimeField(default=datetime.now())
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    expected_time = models.IntegerField(default=15) # Expected Waiting time in minutes
    finalized = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    #json = JSONField(encoder="")

class OrderedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5)
    
    def calculate_price(self):
        self.price = self.item.rate * self.quantity
        
        return self.price

# Create your models here.
