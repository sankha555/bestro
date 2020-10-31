from django.contrib import admin
from items.models import Item, Combo

admin.site.register([Item, Combo])

# Register your models here.
