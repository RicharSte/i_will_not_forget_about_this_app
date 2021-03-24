"""protraker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from todostuff.views import todoappView, addTodo, donetodo
from users.views import register 
from statistic.views import day_statistic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoappView, name='todo-home'), #базовая страница
    path('addTodo/', addTodo),#нужно для добавления задачи
    path('donetodo/<int:item>/', donetodo), #нужно для удаления задачи
    path('register/', register, name='register'),#для регистрации пользователя
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#для логина пользователя
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),#для того,чтобы выйти из учетной записи
    path('my-statistic/', day_statistic, name='statistic'),#чтобы посмотреть статистику
]
