# Generated by Django 5.0.3 on 2024-05-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitbybit', '0003_task_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='index',
        ),
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
