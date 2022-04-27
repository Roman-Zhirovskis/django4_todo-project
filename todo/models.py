from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True) # (blank=True)its meane that this feald is not important
    created = models.DateTimeField(auto_now_add=True)
    datecomplated = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)# необязательный параметр
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Если работаем с текстовыми полями, то blank
    #Если работаем с полями времени, то null
    def __str__(self):
        return self.title