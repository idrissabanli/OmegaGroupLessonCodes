from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'ad': 'Idris', 
        'soyad': 'Sabanli'
    }
    return render(request, 'index.html', context)


def recipes(request):
    return render(request, 'recipes.html')


def sum(a, b):
    return a + b

