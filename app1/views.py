from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def wish(request):
    return HttpResponse('Hi There all! This is Django. How Can I help You?')

def reply(request):
    return HttpResponse('Yes Hi! I\'m Pavi I want to learn')
