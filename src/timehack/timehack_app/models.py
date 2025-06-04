from django.contrib.auth.models import User
from django.db import models


class ListOfTasks(models.Model):
    name = models.CharField('Name', max_length=30)
    description = models.TextField('Description')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Owner')


class Task(models.Model):
    name = models.CharField('Name', max_length=30)
    description = models.TextField('Description')
    done = models.BooleanField('Done', default=False)
    list_of_tasks = models.ForeignKey(
        ListOfTasks, on_delete=models.CASCADE, verbose_name='List')


class SubTask(models.Model):
    name = models.CharField('Name', max_length=30)
    description = models.TextField('Description')
    done = models.BooleanField('Done', default=False)
    # Change This name
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, verbose_name='Task')
