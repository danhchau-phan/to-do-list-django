from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'todoapp/index.html', context)

def remove(request, item_id):
    item = Item.objects.get(id=item_id)
    item.done = True
    item.save()
    return redirect('/todoapp/index/')

def detail(request):
    if request.method == "POST":
        new_item_text = request.POST.get("new_item", None)
        new_item = Item(text=new_item_text, done=False)
        new_item.save()

    return render(request, 'todoapp/detail.html', {})