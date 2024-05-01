from django.shortcuts import render, HttpResponse

def tasks(request):
    return render(request, "tasks.html")