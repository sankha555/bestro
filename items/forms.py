from django import forms
from items.models import Item, Combo 

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['name', 'description', 'category', 'rate', 'stock', 'is_non_veg', 'image']
        
class ComboForm(forms.ModelForm):
    
    class Meta:
        model = Combo
        fields = ['name', 'description', 'rate', 'item1', 'item2', 'item3', 'item4', 'item5', 'image']