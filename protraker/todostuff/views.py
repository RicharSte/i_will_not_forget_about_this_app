from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Todo

def todoappView(request):
    all_todo_items = Todo.objects.all()
    return render(request, 'todo/home.html', {'all_items':all_todo_items, 'title': 'Add some tasks'})

def addTodo(request):
    text = request.POST['content']
    new_todo = Todo(content = text)
    new_todo.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodo(request, item):
    delete_item = Todo.objects.get(id= item)
    delete_item.delete()
    return HttpResponseRedirect('/todoapp/')

