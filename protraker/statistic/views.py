from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todostuff.models import Todo

from datetime import date, timedelta
"""
Эти модули отвечают за всю статистику, которую видет пользователь. Мы считаем, сколько пользователь сделал за сегодня, сколько ему ещё осталось, сколько было сделанно за неделю и за месяц.
"""
@login_required(login_url='login')
def day_statistic(request):
    undone_today = len(Todo.objects.filter(autor_id = request.user, done = 0, done_date = date.today()))
    done_today = len(Todo.objects.filter(autor_id = request.user, done = 1, done_date = date.today()))
   
    week_work = done_in_one_period(request, date.today()-timedelta(days=7), date.today())
    month = done_in_one_period(request, date.today()-timedelta(days=30), date.today())
    
    if done_today + undone_today != 0:
        done_in_percentage = "{:.2f}".format((done_today/(done_today + undone_today)) * 100)
        
        context = {
            'undone_today':undone_today,
            'done_in_percentage': done_in_percentage,
            'week_work':week_work,
            'month':month
        }
        
        return render(request, 'statistic/home.html', context)
    else:
        text = '0'
        return render(request, 'statistic/home.html', {'done_in_percentage': text})
    

def daterange(date1, date2):
    for n in range(int ((date2-date1).days)+1):
        yield date1 + timedelta(n)
        
def done_in_one_period(request, date1, date2):
    tasks = 0
    for date in daterange(date1, date2):
        tasks += len(Todo.objects.filter(autor_id = request.user, done = 1, done_date = date))
        
    return tasks
    