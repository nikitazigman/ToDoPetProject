from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.status


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    number_done_tasks = models.IntegerField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    title = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.strftime("%m/%d/%Y")

    class Meta:
        ordering = ['title']
