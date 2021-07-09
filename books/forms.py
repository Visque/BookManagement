from django.forms import ModelForm
from django.db.models import fields
from django.forms.widgets import Select, TextInput
from books.models import BookInfo

class Create(ModelForm):
    class Meta:
        model = BookInfo
        fields = ['name', 'author', 'genre', 'language']
        widgets={
            'name': TextInput(attrs={'class' : 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'genre': Select(attrs={'class': 'form-control'}),
            'language': Select(attrs={'class': 'form-control'}),
        }