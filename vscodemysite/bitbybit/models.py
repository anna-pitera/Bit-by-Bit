from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_index = models.IntegerField(default=1)
    task_title = models.CharField(max_length=70, unique=True)
    task_desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    is_complete = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # Check if it's a new task being added
        if not self.pk:
            # Get the highest task_index value
            highest_index_task = Task.objects.order_by('-task_index').first()
            if highest_index_task:
                self.task_index = highest_index_task.task_index + 1
        super(Task, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.task_title