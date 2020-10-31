from django.urls import path
from orders.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('new_order', create_order, name='create_order'),
    
    path('<int:pk>/menu', add_items, name='add_items'),
    
    path('<int:pk>/confirm', finalize_order, name='finalize_order'),
        
    path('<int:pk>/delete', delete_order, name='delete_order'),
    
    path('<int:pk>/summary', order_summary, name='order_summary'),
    
    path('<int:pk>/confirm_delivery', accept_order, name='accept_order'),
    
    path('<int:pk>/feedback', feedback, name='feedback'),
    
    path('history', past_transactions, name='past_transactions'),
    
    path('generate_sales', generate_sales, name='generate_sales'),
    
    path('notify_offers', notify_offers, name='notify_offers'),
    
    
    path('menu', test_menu, name='menu'),
    
]
