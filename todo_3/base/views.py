from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


#Detail To Do Element
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

#Create To Do Element
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
