from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ListItem

# Create your views here.
def index(request):
    context = {
        'list_of_items': ListItem.objects.all(),
        }
    return HttpResponse(loader.get_template('todolist_app/index.html').render(context, request))
