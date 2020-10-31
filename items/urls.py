from django.urls import path
from items.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('create_item', create_item, name='create_item'),
    
    path('<int:pk>/update_item', update_item, name='update_item'),
    
    #path('create_combo', create_combo, name='create_combo'),
    
    #path('<int:pk>/update_combo', update_combo, name='update_combo'),
    
]
