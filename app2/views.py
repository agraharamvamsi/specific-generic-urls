from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sujitha(request):
    return HttpResponse('<h1>I got placed in google <h1/>')

def meena(request):
    return HttpResponse('<h1>meena is good girl</h1>')
