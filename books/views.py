from books.models import BookInfo
from django.shortcuts import render, redirect
from books.forms import Create
from books.models import GENRE_CHOICES, LANGUAGE_CHOICES
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    form = Create()
    formFilled = False
    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            formFilled = True
            form=Create()
            variables = {'form': form, 'formFilled': formFilled}
            return render(request, 'books/create.html', context=variables)
        else:
            print("error raised: Form is invalid")
            return render(request, 'index.html')
    variables = {'form': form, 'formFilled': formFilled}
    return render(request, 'books/create.html', context=variables)

def display(request):
    books = BookInfo.objects.all()
    genres = list()
    languages = list()
    for i in GENRE_CHOICES:
        genres.append(i[1])
    for j in LANGUAGE_CHOICES:
        languages.append(j[1])
    print("gnre", genres)
    variables = {'books': books, 'genres': genres, 'languages': languages}
    return render(request, 'books/display.html', context=variables)