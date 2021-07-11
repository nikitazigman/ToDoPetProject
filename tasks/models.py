from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from dashboard.models import List


class Status(models.Model):
    status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.status


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    difficulty = models.IntegerField(default=0)
    moved_number = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now())

    task_list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['difficulty']