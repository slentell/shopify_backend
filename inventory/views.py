from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from .models import Inventory
from .forms import  ItemForm, DeleteForm

# Create your views here.
def get_item(inventory_id):
    return Inventory.objects.get(inventory_id)

def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'items':items})

def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('inventory_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def edit_item(request, inventory_id):
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            item.save()
        return redirect('inventory_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})


def temp_delete(request, inventory_id):
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        form = DeleteForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            item.deleted=True
            item.save(update_fields=['deleted'])
        return redirect('deleted_items')
    else:
        form = DeleteForm(instance=item)
    return render(request, 'temp_delete.html', {'form': form})

def restore_deleted_item(request, inventory_id):
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        item.deleted=False
        item.save(update_fields=['deleted'])
        return redirect('inventory_list')
    return render(request, 'restore_item.html', {'item':item} )

def deleted_item_list(request):
    context = {'items' : Inventory.objects.all()}
    return render(request, 'deleted_items.html', context=context)



def true_delete_item(request, inventory_id):
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect('/')
    return render(request, 'true_delete.html')



