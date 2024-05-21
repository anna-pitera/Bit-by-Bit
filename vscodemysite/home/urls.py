from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from bitbybit import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("admin/", admin.site.urls),
    path("<int:task_index>/complete_task/", views.complete_task, name="complete_task"),
    path("/create_task/", views.create_task, name="create_task"),
]