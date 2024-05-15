from django.db import models

class Task(models.Model):
    class Meta:
        app_label = 'bitbybit'
    
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text