from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, date
class Todo(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    done_date = models.DateField(auto_now=True)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    