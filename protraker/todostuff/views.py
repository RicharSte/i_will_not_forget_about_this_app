from django.shortcuts import render

def todo_add(request):
    return render(request, 'index.html')

