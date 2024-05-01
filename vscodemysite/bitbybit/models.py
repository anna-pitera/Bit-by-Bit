from django.db import models

class Task(models.Model):
    task_title = models.CharField(max_length=70)
    task_desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)