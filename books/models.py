from django.db import models

# Create your models here.
GENRE_CHOICES =[
    ("1", "Educational"),
    ("2", "Fairy Tales"),
    ("3", "Mystery"),
    ("4", "Fictional"),
]

LANGUAGE_CHOICES =[
    ("1", "English"),
    ("2", "German"),
    ("3", "Chinese"),
    ("4", "French"),
    ("5", "Japanse"),
]

class BookInfo(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=80, choices=GENRE_CHOICES)
    language = models.CharField(max_length=80, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.name