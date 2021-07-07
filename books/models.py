from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    language = models.CharField(max_length=80)

    def __str__(self):
        return self.name