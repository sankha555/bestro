from django.contrib import admin
from users.models import Customer, Staff

admin.site.register([Customer, Staff])

# Register your models here.
