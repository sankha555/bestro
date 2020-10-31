from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from items.models import Item, Combo
from items.forms import ItemForm, ComboForm

@staff_member_required
def create_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            messages.success(request, f'Item Added to Menu!')
            
            return redirect('menu')
        
    else:
        form = ItemForm()
        
    context = {
        'form' : form
    }
    return render(request, 'items/create_item.htm', context)
        
@staff_member_required
def update_item(request, pk):
    
    item = get_object_or_404(Item, pk = pk)
    
    if request.method == "POST":
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            
            form.save()
            messages.success(request, f'Item Updated!')
            
            return redirect('menu')
        
    else:
        form = ItemForm(instance = item)
        
    context = {
        'form' : form,
        'item' : item
    }
    return render(request, 'items/update_item.htm', context)

@staff_member_required
def create_combo(request):
    if request.method == "POST":
        form = ComboForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('create_combo')
        
    else:
        form = ComboForm()
        
    context = {
        'form' : form
    }
    return render(request, 'combos/create_combo.htm', context)
        
@staff_member_required
def update_combo(request, pk):
    
    combo = get_object_or_404(Combo, pk = pk)
    
    if request.method == "POST":
        form = ComboForm(request.POST, instance = combo)
        if form.is_valid():
            
            form.save()
            return redirect('create_combo')
        
    else:
        form = ComboForm(instance = combo)
        
    context = {
        'form' : form,
        'combo' : combo
    }
    return render(request, 'items/create_combo.htm', context)


# Create your views here.
