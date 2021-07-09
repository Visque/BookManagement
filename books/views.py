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
    # for passing all genre and languages to pass in the multichoice dropdown field
    languages = list()
    genres = list()
    for i in GENRE_CHOICES: 
        genres.append(i[1])                 # index 1 since zeroeth( 0 ) position has ID
    for j in LANGUAGE_CHOICES:
        languages.append(j[1])              # index 1 since zeroeth( 0 ) position has ID

    # for POST request  :-

    if request.method == 'POST':
        genreList = request.POST.get('genreSelected').strip().split(",")
        languageList = request.POST.get('languageSelected').strip().split(",")
        print("genre: ", genreList, languageList)
        if genreList[0] == '':
            print("genre empty")
            attributes = languageList
            if languageList[0] == '':
                return redirect('/display')
        elif languageList[0] == '':
            print("language empty")
            attributes = genreList
        else:
            attributes = genreList + languageList
        searchList = list()
        print("attributes: ", attributes)
        for attribute in attributes:
            print("attribute: ", attribute)
            if len(BookInfo.objects.filter(genre = attribute)):
                items = BookInfo.objects.filter(genre = attribute)
                for object in items:
                    searchList.append(object)
            elif len(BookInfo.objects.filter(language = attribute)):
                items = BookInfo.objects.filter(language = attribute)
                for object in items:
                    searchList.append(object)
            else:
                books = None
                variables = {'books': books, 'genres': genres, 'languages': languages}
                return render(request, 'books/display.html', context=variables)
        print("hahahahaha: ", searchList)
        searchset = set(searchList)
        print("mahahahaha: ", searchset)
        variables = {'books': searchset, 'genres': genres, 'languages': languages}
        return render(request, 'books/display.html', context=variables)
    # for normal accesss
    else: 
        books = BookInfo.objects.all()
        variables = {'books': books, 'genres': genres, 'languages': languages}
        return render(request, 'books/display.html', context=variables)

