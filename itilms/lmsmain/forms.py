from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Category
        fields = ['name']
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'photo_book', 'photo_author', 'pages', 'price', 'rent_day', 'rent_period','rent_price', 'status', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_author': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent_day': forms.NumberInput(attrs={'class': 'form-control','id':'rp'}),
            'rent_period': forms.NumberInput(attrs={'class': 'form-control','id':'rd'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control','id':'rt'}),
        }