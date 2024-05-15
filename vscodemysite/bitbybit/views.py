from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from bitbybit.models import Task

def create_task(request):
    all_tasks = Task.objects.all()
    if "create" in request.POST:
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title, desc)
        ins = Task(task_title=title, task_desc=desc)
        ins.save()
        context = {"tasks": all_tasks}
    context = {"tasks": all_tasks}
    return render(request, "tasks.html", context)

def complete_task(request, task_index):
    all_tasks = Task.objects.all()
    task = get_object_or_404(Task, pk=task_index)
    task.is_complete = True
    task.save()
    context = {"tasks": all_tasks}
    print("task completed")
    return render(request, "tasks.html", context)