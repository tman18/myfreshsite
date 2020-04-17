from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render
import requests
def index(request):
    context = {
        'request': request
    }
    return render(request, "content/index.html", context)

def about_me(request):
    context = {
        'request': request
    }
    return render(request, "content/about-me.html", context)

def resume(request):
    response = requests.get('https://api.github.com/users/tman18/repos')
    repos = response.json()
    context = {
        'request': request,
        'response': response,
        'repos': repos,
    }
    return render(request, "content/resume.html", context)

def contact(request):
    context = {
        'request': request
    }
    return render(request, "content/contact.html", context)