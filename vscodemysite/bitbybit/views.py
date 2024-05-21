from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bitbybit.models import Task

@login_required
def task_list(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'tasks.html', {'tasks': tasks})
    else:
        return render(request, 'login.html')

@login_required
def create_task(request):
    print(request.method)
    print("help")
    if request.method == "POST":
        tasks = Task.objects.filter(user=request.user)
        print("sad")
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        user = request.user
        print(title, desc)
        Task.objects.create(task_title=title, task_desc=desc, user=user)
        return redirect('task_list')
    return render(request, "tasks.html", {'tasks': tasks})

@login_required
def complete_task(request, task_index):
    all_tasks = Task.objects.all()
    task = get_object_or_404(Task, pk=task_index)
    task.is_complete = True
    task.save()
    context = {"tasks": all_tasks}
    print("task completed")
    return render(request, "tasks.html", context)