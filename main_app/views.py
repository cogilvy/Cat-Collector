from django.shortcuts import render
from django.http import HttpResponse
from .models import cats as cats

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello World!</h1>')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html', {'cats': cats})