from django.db import models

# Create your models here.
GENRE_CHOICES =[                                                        # Add your custom Genre here 
    ("Educational", "Educational"),
    ("Fairy Tales", "Fairy Tales"),
    ("Mystery", "Mystery"),
    ("Fictional", "Fictional"),
]

LANGUAGE_CHOICES =[                                                      # add your custom language here
    ("English", "English"),
    ("German", "German"),
    ("Chinese", "Chinese"),
    ("French", "French"),
    ("Japanese", "Japanese"),
]

class BookInfo(models.Model):                                             # A calss used to store information about books
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=80, choices=GENRE_CHOICES)          # genre is taken as char fields because it is stored in a text field and then retrieved though in UI it may seem to be chosen from select field
    language = models.CharField(max_length=80, choices=LANGUAGE_CHOICES)    # same goes for language field as well

    def __str__(self):
        return self.name