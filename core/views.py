from multiprocessing import context
from django.shortcuts import render, redirect


def homepage(request):
    context = {
        'homepage_text': "Welcome to the Homepage"
    }
    return render(request, 'homepage.html', context)


def contact(request):
    context = {
        'contact_text': "Welcome to the Contact us page"
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "Welcome to the About us page"
    }
    return render(request, 'about.html', context)
