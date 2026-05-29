from todo_main import urls
from django.urls import path
from .import views 

urlpatterns = [
    path('addTask/',views.addTask,name = 'addTask'),
]