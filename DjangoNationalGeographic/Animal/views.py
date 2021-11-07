from django.shortcuts import render
from django.views.generic import View
import requests

def home(request):
    context = {}
    response = requests.get('http://127.0.0.1:8000/api/animal/')
    animals = response.json()

    context["animals"] = animals
    
    return render(request, 'home.html', context)
    
