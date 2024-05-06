from django.shortcuts import render, HttpResponse
from bitbybit.models import Task

def tasks(request):
    all_tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title, desc)
        ins = Task(task_title=title, task_desc=desc)
        ins.save()
        context = {"tasks": all_tasks}
    context = {"tasks": all_tasks}
    return render(request, "tasks.html", context)