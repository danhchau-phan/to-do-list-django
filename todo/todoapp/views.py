from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Task
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


def updatestatus(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id", None)
        new_status = request.POST.get("new_status", None)
        task = Task.objects.all().get(id=int(task_id))
        setattr(task, 'status', new_status)
        task.save()
    return index(request)

def index(request):
    try:
        tasks1 = Task.objects.filter(assignee = request.user)
    except ObjectDoesNotExist: # Error is raised if 0 tasks
        tasks1 = []

    try:
        tasks2 = Task.objects.filter(assigner = request.user)
    except ObjectDoesNotExist: # Error is raised if 0 tasks
        tasks2 = []
     # alt: items = request.user.task_set.all(), no exception handling needed
    
    context = {
        'user': request.user,
        'tasks1': tasks1,
        'tasks2': tasks2
    }
    return render(request, 'todoapp/index.html', context)

# @method_decorator(require_POST)
def remove(request, task_id):
    # a task can only be removed by its assigner
    if request.method == "POST":
        task = Task.objects.filter(id=task_id).delete()
    return redirect('/todoapp/index/')

def add(request):
    if request.method == "POST":
        description = request.POST.get("new_task", None)
        deadline = request.POST.get("deadline", None)
        assignee = get_user_model().objects.get(username=request.POST.get("assignee", None))
        new_item = Task(text=text, deadline=deadline, assignee=assignee, assigner=request.user)
        new_item.save()

    return render(request, 'todoapp/add.html', {'users': get_user_model().objects.all()})

def manage(request):
    user = request.user
    context = {
        'user': user,
        'groups': Group.objects.filter(),
        'remained_groups': Group.objects.filter()
    }
    return render(request, 'todoapp/manage.html', context)

# def detail(request, task_id):
#     # assignee's view of task detail
#     task = request.user.task_set.get(id=task_id)
#     return render(request, 'todoapp/detail.html', {"task": task, "assigner": False})

# def detail_assigner(request, task_id):
#     # assignee's view of task detail
#     return render(request, 'todoapp/detail.html', {"assigner": True})




