from django.db import models

# Create your models here.
GENRE_CHOICES =[
    ("Educational", "Educational"),
    ("Fairy Tales", "Fairy Tales"),
    ("Mystery", "Mystery"),
    ("Fictional", "Fictional"),
]

LANGUAGE_CHOICES =[
    ("English", "English"),
    ("German", "German"),
    ("Chinese", "Chinese"),
    ("French", "French"),
    ("Japanese", "Japanese"),
]

class BookInfo(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=80, choices=GENRE_CHOICES)
    language = models.CharField(max_length=80, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name