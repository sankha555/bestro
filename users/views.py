from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from users.models import Customer, Staff
from users.forms import UserRegistrationForm, CustomerProfileForm, StaffProfileForm

def post_login(request):
    if request.user.is_superuser:
        return redirect('staff_dashboard')
    else:
        return redirect('customer_dashboard')

def register_customer(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()

            username = user_form.cleaned_data["username"]
            pwd = user_form.cleaned_data["password1"]
            
            auth_user = authenticate(username=username, password=pwd)
            login(request, auth_user)
            
            customer = customer_form.instance         
            customer.user = auth_user
            customer.email = auth_user.email
            customer.save()
            
            messages.success(request, f'Welcome to Bistro! Happy Fooding!')
            
            return redirect('customer_dashboard')
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerProfileForm()
    
    context = {
        'uform' : user_form,
        'cform' : customer_form
    }
    
    return render(request, 'users/register_customer.htm', context)

@login_required
def customer_dashboard(request):
    
    user = request.user
    if not user.is_superuser:
        if not Customer.objects.filter(user = user).exists():
            
            customer = Customer.objects.create(
                user = user,
            )
            customer.save()
            messages.success(request, f'Please Update Your Profile to Help us serve You Better!')
            
            return redirect('customer_profile')

        else:
            customer = get_object_or_404(Customer, user = user)
        
        if customer.name == "" or customer.address == "" or customer.phone == "":
            messages.success(request, f'Please Update Your Profile to Help us serve You Better!')
            return redirect('customer_profile')
        
        context = {
            'customer' : customer
        }
        
        return render(request, 'users/customer_dashboard.htm', context)
   
@login_required 
def customer_profile(request):
    
    customer = get_object_or_404(Customer, user = request.user)
    
    if request.method == "POST":
        
        form = CustomerProfileForm(request.POST, request.FILES, instance = customer)
        
        if form.is_valid():
            form.save()
            customer.email = request.user.email
            customer.save()
            
            messages.success(request, f'Profile Updated!')
            return redirect('customer_dashboard')
        
    else:
        form = CustomerProfileForm(instance = customer)
    
    context = {
        'customer' : customer,
        'form' : form
    }    
    
    return render(request, 'users/customer_profile.htm', context)


# Staff Methods

@staff_member_required
def register_staff(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        staff_form = StaffProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and staff_form.is_valid():
            user_form.save()

            user = user_form.instance
            user.is_superuser = True
            user.is_staff = True
            user.save()
            
            #auth_user = authenticate(username=username, password=pwd)
            #login(request, auth_user)
            
            staff = staff_form.instance         
            staff.user = user
            staff.email = user.email
            staff.save()
            
            return redirect('staff_dashboard')
    else:
        user_form = UserRegistrationForm()
        staff_form = StaffProfileForm()
    
    context = {
        'uform' : user_form,
        'cform' : staff_form
    }
    
    return render(request, 'users/register_staff.htm', context)

@staff_member_required
def staff_dashboard(request):
    
    user = request.user
    if user.is_superuser:
        if not Staff.objects.filter(user = user).exists():
            
            staff = Staff.objects.create(
                user = user
            )
            staff.save()
            
            return redirect('staff_profile')

        else:
            staff = get_object_or_404(Staff, user = user)
        
        context = {
            'staff' : staff
        }
        
        return render(request, 'users/staff_dashboard.htm', context)
  
@staff_member_required  
def staff_profile(request):
    
    staff = get_object_or_404(Staff, user = request.user)
    
    if request.method == "POST":
        
        form = StaffProfileForm(request.POST, request.FILES, instance = staff)
        
        if form.is_valid():
            form.save()
            staff.email = request.user.email
            staff.save()
            
            return redirect('staff_dashboard')
        
    else:
        form = StaffProfileForm(instance = staff)
    
    context = {
        'staff' : staff,
        'form' : form
    }    
    
    return render(request, 'users/staff_profile.htm', context)


# Create your views here.
