from django.shortcuts import render,  redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse

def addTask(request):
    task = request.POST.get('task') #to get the value of task from the form 
    Task.objects.create(task = task) # to create a new task in the database 
    return redirect ('home')

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    # return HttpResponse(f'Mark as done {pk}')
    return redirect('home')

def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def mark_as_undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method=='POST':
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')
    else :
        context={
            'task': task,
        }
  
    return render(request, 'edit_task.html', context)

# def updateTask(request, pk):
#     get_task = get_object_or_404(Task, pk=pk)

#     return redirect('home')