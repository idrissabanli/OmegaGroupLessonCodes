from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
    s = 'salam necesen?'
    context = {
        'stories': story_list,
        's': s
    }
    return render(request, 'stories.html', context)


def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    context = {
        'story': story
    }
    return render(request, 'single.html', context)

