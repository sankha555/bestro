from orders.models import Order, OrderedItem
from items.models import Item, Combo
from django.contrib.auth.models import User
import smtplib
from django.conf import settings
from django.core.mail import send_mail

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def calculate_grand_total_and_update_stocks(order, ordered_items):
    
    grand_total = 0
    for o_item in ordered_items:
        
        o_item.item.stock -= o_item.quantity
        grand_total += o_item.calculate_price()
        o_item.save()
        
    order.grand_total = grand_total
    order.save()
    
def calculate_expected_delivery_time(order):
    
    active_orders = Order.objects.filter(finalized=True, delivered = False)
    expected_del_time = active_orders.count() * 15 + 15
    
    order.expected_time = expected_del_time
    order.save()
    
def calculate_item_ratings(ordered_items):
    
    for o_item in ordered_items:
        count_item = OrderedItem.objects.filter(item = o_item.item).count()
        curr_rating_total = (o_item.item.rating * count_item) + o_item.rating
        
        curr_rating = (curr_rating_total)/(count_item + o_item.quantity)
        
        o_item.item.rating = curr_rating
        o_item.item.save()
        o_item.save()
        
def mail_customers(customers, offer_text):
    
    for customer in customers:
        
        send_mail(
            'New Offer from Bestro!',
            offer_text,
            'backdev2020@gmail.com',
            [customer.user.email],
            fail_silently=False,
        )
                