from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d")

    class Meta:
        ordering = ['-date']
