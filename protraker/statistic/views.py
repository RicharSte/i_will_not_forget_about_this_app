from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todostuff.models import Todo

from datetime import date

@login_required(login_url='login')
def day_statistic(request):
    undone_today = len(Todo.objects.filter(autor_id = request.user, done = 0, done_date = date.today()))
    done_today = len(Todo.objects.filter(autor_id = request.user, done = 1, done_date = date.today()))
    
    done_in_percentage = "{:.2f}".format((done_today/(done_today + undone_today)) * 100)
    
    context = {
        'undone_today':undone_today,
        'done_in_percentage': done_in_percentage
    }
    
    return render(request, 'statistic/home.html', context)