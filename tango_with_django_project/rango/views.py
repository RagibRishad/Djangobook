from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    show = { 'boldmessage': 'Hello. you alright!'}
    return render(request, 'rango/index.html', context=show)