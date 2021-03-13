from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Todo

def todoappView(request):
    all_todo_items = Todo.objects.filter(autor_id = request.user)
    return render(request, 'todo/home.html', {'all_items':all_todo_items, 'title': 'Add some tasks'})

def addTodo(request):
    text = request.POST['content']
    new_todo = Todo(content = text)
    new_todo.autor = request.user
    new_todo.save()
    return redirect ('todo-home')

def deleteTodo(request, item):
    delete_item = Todo.objects.get(id= item)
    delete_item.delete()
    return redirect ('todo-home')

