from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def contacts_view(request):
    return HttpResponse('<h1>Contacts</h1>')

def about_view(request):
    return HttpResponse('<h1>About</h1>')
