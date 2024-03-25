from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'tasks': tasks, 'form': form}
    return render(request, '../templates/index.html', context)