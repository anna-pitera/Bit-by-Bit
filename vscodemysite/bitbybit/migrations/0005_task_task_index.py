# Generated by Django 5.0.3 on 2024-05-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitbybit', '0004_remove_task_index_task_id_alter_task_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_index',
            field=models.IntegerField(default=1),
        ),
    ]
