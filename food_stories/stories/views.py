from django.shortcuts import render
from django.http import HttpResponse
from stories.models import Story


def home(request):
    context = {
        'ad': 'Idris', 
        'soyad': 'Sabanli'
    }
    return render(request, 'index.html', context)


def recipes(request):
    return render(request, 'recipes.html')


def stories(request):
    story_list = Story.objects.all()
    context = {
        'stories': story_list
    }
    return render(request, 'stories.html', context)


