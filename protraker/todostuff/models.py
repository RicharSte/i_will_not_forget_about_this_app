from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    content = models.TextField()
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    