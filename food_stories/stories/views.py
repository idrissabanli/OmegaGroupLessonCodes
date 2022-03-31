from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from stories.models import Story
from stories.forms import ContactForm


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


def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
            return redirect(reverse_lazy('home'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def like_story(request, id):
    request.session['liked_stories']= f"{request.session.get('liked_stories', '')} {id}"
    print('request.session', request.session['liked_stories'])
    messages.add_message(request, messages.SUCCESS, 'Siz mehsulu beyendiniz!')
    return redirect(reverse_lazy('home'))


def liked_stories(request):
    liked_stories = request.session.get('liked_stories',)
    stories = None
    if liked_stories:
        print('liked_stories', 3*'\n', liked_stories, 3*'\n',)
        splited_liked_stories = liked_stories.split()
        print(splited_liked_stories)
        liked_stories = list(map(int, splited_liked_stories))
        print(liked_stories)
        stories = Story.objects.filter(id__in=liked_stories)
    context = {
        'stories': stories
    }
    return render(request, 'liked_stories.html', context)


