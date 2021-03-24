from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#мы создаем форму, для того, чтобы добавить поле имейла во время регистрации
class UserRegiesterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']