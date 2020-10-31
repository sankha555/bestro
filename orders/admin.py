from django.contrib import admin
from orders.models import Order, OrderedItem

admin.site.register([Order, OrderedItem])

# Register your models here.
