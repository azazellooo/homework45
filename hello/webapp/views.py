from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from webapp.models import Task, status_choices

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})

def task_create_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', context={"choices": status_choices})
    elif request.method == "POST":
        description = request.POST.get("description")
        text = request.POST.get("text")
        status = request.POST.get("status")
        date = request.POST.get("date")
        if date == "":
            date = None
        task = Task.objects.create(
            description=description,
            text=text,
            status=status,
            date=date
        )
        return redirect('task-view', pk=task.id)
# Create your views here.
