from django.shortcuts import render
from .models import Item
# Create your views here.

def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'todoapp/index.html', context)

def detail(request):
    if request.method == "POST":
        new_item_text = request.POST.get("new_item", None)
        new_item = Item(text=new_item_text, done=False)
        new_item.save()

    return render(request, 'todoapp/detail.html', {})