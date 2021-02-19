from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Task
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    try:
        tasks = Task.objects.filter(assignee = request.user)
    except ObjectDoesNotExist: # Error is raised if 0 tasks
        tasks = []
     # alt: items = request.user.task_set.all(), no exception handling needed
    
    context = {
        'user': request.user,
        'items': tasks
    }
    return render(request, 'todoapp/index.html', context)

def remove(request, task_id):
    if request.method == "POST":
        user = request.user
        task = user.task_set.get(id=task_id)
        task.done = True
        task.save()
    return redirect('/todoapp/index/')

def add(request):
    if request.method == "POST":
        text = request.POST.get("new_task", None)
        deadline = request.POST.get("deadline", None)
        assignee = get_user_model().objects.get(username=request.POST.get("assignee", None))
        new_item = Task(text=text, deadline=deadline, done=False, assignee=assignee, assigner=request.user)
        new_item.save()

    return render(request, 'todoapp/add.html', {'users': get_user_model().objects.all()})

def detail(request, task_id):
    # assignee's view of task detail
    task = request.user.task_set.get(id=task_id)
    return render(request, 'todoapp/detail.html', {"task": task, "assigner": False})

def detail_assigner(request, task_id):
    # assignee's view of task detail
    return render(request, 'todoapp/detail.html', {"assigner": True})




