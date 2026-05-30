from django.shortcuts import render 
from django.http import HttpResponse 
from todos.models import Task

def home (request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at') # to get all the tasks from the database and order them by created_at in descending order
    completed_task = Task.objects.filter(is_completed=True).order_by('-created_at') # to get all the completed tasks and order them by created_at in descending order
    context = {
        'tasks': tasks,
        'completed_task': completed_task,
    }
    return render(request,'home.html', context)