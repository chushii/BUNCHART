"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PoolForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/contact.html',
        {
            'title':'Контакты',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/about.html',
        {
            'title':'О проекте',
            'year':datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/links.html',
        {
            'title':'Ссылки',
            'year':datetime.now().year,
        }
    )

def pool(request):
    data = None
    gender = { '1': 'Мужской', '2': 'Женский' }
    grade = { '1': 'Ужасно', '2': 'Плохо', '3': 'Нормально',
        '4': 'Хорошо', '5': 'Отлично' }
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['grade'] = grade[form.cleaned_data['grade']]
            data['recom'] = 'Да' if form.cleaned_data['recom'] else 'Нет'
            data['advice'] = form.cleaned_data['advice']
            form = None
    else:
        form = PoolForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/pool.html',
        {
            'title':'Обратная связь',
            'form':form,
            'data':data,
            'year':datetime.now().year,
        }
    )
    
def signup(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('home')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'main/signup.html',
        {
            'regform': regform,
            'title':'Регистрация',
            'year':datetime.now().year,
        }
    )
