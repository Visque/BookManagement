from django import forms
from django.db.models import fields
from books.models import BookInfo

class Create(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ['name', 'author', 'genre', 'language']
