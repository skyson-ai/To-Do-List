# Generated by Django 5.1.6 on 2025-02-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_on',
        ),
    ]
