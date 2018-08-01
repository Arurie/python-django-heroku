#views are the pages

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'game/index.html', context)

def contact(request):
    context = {}
    return render(request, 'game/contact.html', context)

def game(request):
    context = {}
    return render(request, 'game/game.html', context)
