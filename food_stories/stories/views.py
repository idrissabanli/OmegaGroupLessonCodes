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

