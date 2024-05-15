from django.contrib import admin
from django.urls import path, include
from bitbybit import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.create_task, name="create_task"),
    path("<int:task_index>/complete_task/", views.complete_task, name='complete_task'),
]