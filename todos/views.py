from django.shortcuts import render,  redirect
from .models import Task

def addTask(request):
    task = request.POST.get('task') #to get the value of task from the form 
    Task.objects.create(task = task) # to create a new task in the database 
    return redirect ('home')
