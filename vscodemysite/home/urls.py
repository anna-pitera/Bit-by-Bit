from django.contrib import admin
from django.urls import path, include
from bitbybit import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.tasks, name="tasks"),
    path("tasks", views.tasks, name="tasks")
]