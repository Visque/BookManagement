from django.shortcuts import render
# from .models import models

# Create your views here.

def index(request):
    return render(request, 'books/index.html')