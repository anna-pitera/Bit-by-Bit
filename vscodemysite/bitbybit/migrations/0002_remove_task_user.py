# Generated by Django 5.0.3 on 2024-05-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitbybit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
