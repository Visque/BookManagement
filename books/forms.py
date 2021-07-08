from django import forms
from django.db.models import fields
from django.forms import widgets
from books.models import BookInfo

class Create(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ['name', 'author', 'genre', 'language']


    widgets={
        'name': forms.TextInput(attrs={"class" : 'form-control'}),
        'author': forms.TextInput(attrs={"class": 'form-control'}),
        'genre': forms.Select(attrs={"class": 'form-control'}),
        'language': forms.Select(attrs={"class": 'form-control'}),
    }