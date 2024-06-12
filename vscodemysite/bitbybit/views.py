from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from bitbybit.models import Task
from bitbybit.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

@login_required
def task_list(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated == True:
        tasks = Task.objects.filter(user=request.user)
        return render(request, "tasks.html", {"tasks": tasks})
    elif request.user.is_authenticated == False:
        return render(request, "login.html")

@login_required
def create_task(request):
    print(request.method)
    if request.method == "POST":
        tasks = Task.objects.filter(user=request.user)
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        user = request.user
        print(title, desc)
        Task.objects.create(task_title=title, task_desc=desc, user=user)
        return redirect('task_list')
    return render(request, "tasks.html", {'tasks': tasks})

@login_required
def complete_task(request, task_id):
    tasks = Task.objects.filter(user=request.user)
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_complete = True
    task.save()
    context = {"tasks": tasks}
    print("task completed")
    return render(request, "tasks.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy("task_list"))
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})