from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Todo

from datetime import date

@login_required(login_url='login')
def todoappView(request):
    done_items = Todo.objects.filter(autor_id = request.user, done = 1, done_date = date.today())
    undine_items = Todo.objects.filter(autor_id = request.user, done = 0)
    
    context = {
        'done':done_items, 
        'undone':undine_items,
        'title': 'Add some tasks'
    }
    
    return render(request, 'todo/home.html', context)

def addTodo(request):
    text = request.POST['content']
    new_todo = Todo(content = text)
    new_todo.autor = request.user
    new_todo.save()
    return redirect ('todo-home')

def donetodo(request, item):
    donetodo = Todo.objects.get(id= item)
    donetodo.done = 1
    donetodo.save()
    return redirect ('todo-home')

