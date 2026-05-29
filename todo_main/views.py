from django.shortcuts import render 
from django.http import HttpResponse 
from todos.models import Task

def home (request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at') # to get all the tasks from the database and order them by created_at in descending order
    
    context = {
        'tasks': tasks,
    }
    return render(request,'home.html', context)