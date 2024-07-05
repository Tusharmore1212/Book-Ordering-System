# books/forms.py
from django import forms
from mybooks.models import Book,Buyerinfo

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price', 'author', 'description', 'image','file','quantity']


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buyerinfo
        fields = ['cname', 'cemail', 'cphone', 'cadd', 'bname','quantity','quantity']