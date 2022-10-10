from web.util.theme import get_theme

from django.shortcuts import render


def index(request):
    context = {
        'theme': get_theme(request)
    }

    return render(request, 'index.html', context=context)