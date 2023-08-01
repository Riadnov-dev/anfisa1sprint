from django.shortcuts import render


def index(request):
    templates = 'homepage/index.html'
    return render(request, templates)
