from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse_lazy
from bitbybit import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("tasks/", views.task_list, name="task_list"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("complete_task/<int:task_id>/", views.complete_task, name='complete_task'),
    path("create_task/", views.create_task, name="create_task")
]