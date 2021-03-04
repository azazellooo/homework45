from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from webapp.models import Task, status_choices
from webapp.forms import TaskForm

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})

def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', context={'choices': status_choices, 'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data.get('description'),
                text=form.cleaned_data.get('text'),
                status=form.cleaned_data.get('status'),
                date=form.cleaned_data.get('date')
            )
            return redirect('task-view', pk=task.id)
        return render(request, 'task_create.html', context={'form': form})

def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
           'description': task.description,
           'text': task.text,
           'status': task.status,
           'date': task.date
        })
        return render(request, 'task_update.html', context={'task': task, 'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.text = form.cleaned_data.get('text')
            task.status = form.cleaned_data.get('status')
            task.date = form.cleaned_data.get('date')
            task.save()
            return redirect('task-view', pk=task.id)
        return render(request, 'task_update.html', context={'form': form, 'task': task})

def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('task-list')
# Create your views here.
