from books.models import BookInfo
from django.shortcuts import render, redirect
from books.forms import Create
from books.models import GENRE_CHOICES, LANGUAGE_CHOICES
# Create your views here.

def index(request):
    return render(request, 'index.html')                                                    # returns the Index page

def create(request):                                                                        # Returns the Create page
    form = Create()
    formFilled = False
    if request.method == 'POST':                                                            # True when a user submits the book information or creates a book
        form = Create(request.POST)
        if form.is_valid():                                                                 # default validator used (No custom validators are made)
            form.save()
            formFilled = True                                                               # variable to be used in html page as a DTL to check whether the form has been filled or not
            form=Create()
            variables = {'form': form, 'formFilled': formFilled}                            # context_variable
            return render(request, 'books/create.html', context=variables)
        else:
            print("error raised: Form is invalid")                                          # Failed validation
            return render(request, 'index.html')
    variables = {'form': form, 'formFilled': formFilled}                                    # Book Yet to be created or submitted
    return render(request, 'books/create.html', context=variables)

def display(request):                                                                       # returns the display page        
    # for passing all genre and languages to pass in the multichoice dropdown field
    languages = list()
    genres = list()
    # saving all the genre and language choices, list to be updated in the books.models.py
    for i in GENRE_CHOICES:                                                                 
        genres.append(i[1])                                                                 # index 1 since 0 index has position has ID
    for j in LANGUAGE_CHOICES:
        languages.append(j[1])                                                              # index 1 since 0 index has position has ID

    # for POST request  :-

    if request.method == 'POST':                                                            # When filtering request submitted
        genreList = request.POST.get('genreSelected').strip().split(",")                    # genreSelected is the name of the readonly text field and all its content is broken and added into a list o
        languageList = request.POST.get('languageSelected').strip().split(",")              # same for languageSelected
        print("genre: ", genreList, languageList)
        
        # condition checks for the list could be empty and raise an error

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
        print("attributes: ", attributes)                                                   # attribute is the final list of all genre and languages to be filtered apart
        for attribute in attributes:
            print("attribute: ", attribute)
            if len(BookInfo.objects.filter(genre = attribute)):                             # checking whether an object with the requested GENRE exists or not
                items = BookInfo.objects.filter(genre = attribute)                          
                for object in items:
                    searchList.append(object)                                               # If True, add it to searchList
            elif len(BookInfo.objects.filter(language = attribute)):                        # checking whether an object with the requested LANGUAGE exists or not
                items = BookInfo.objects.filter(language = attribute)
                for object in items:
                    searchList.append(object)                                               # If True, add it to searchList
            else:                                                                           # True if no attributes matched and is returns nothing (None)
                continue                                                                    # CHANGE #2
        searchset = set(searchList)                                                         # Since the matched objects were added to a list (searchList), duplicates may be present so the list is converted to a set to remove the duplicates
        variables = {'books': searchset, 'genres': genres, 'languages': languages}
        return render(request, 'books/display.html', context=variables)

    # FOR normal accesss (NOT A POST REQUEST) :-

    else: 
        books = BookInfo.objects.all()
        variables = {'books': books, 'genres': genres, 'languages': languages}
        return render(request, 'books/display.html', context=variables)

