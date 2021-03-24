from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, date

#модель задачи. нам нужно знать: сделана ли она, кто её сделал, что это за задача и время создания и когда она была изменина(когда задача была завершенна)
class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    done_date = models.DateField(auto_now=True)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    