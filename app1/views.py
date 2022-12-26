from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dinesh(request):
    return HttpResponse('<h1> This is my app1 first view<h1>')
def praveen(request):
    return HttpResponse('<h2>This is my app1 secoend view</h2>')