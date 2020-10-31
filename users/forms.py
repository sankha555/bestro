from django import forms 
from users.models import Customer, Staff
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
            
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'image']

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'phone', 'image']
        
