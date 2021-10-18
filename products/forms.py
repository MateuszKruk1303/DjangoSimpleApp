from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price']

class ProductEditForm(forms.Form):
    new_name = forms.CharField(label='New name', max_length=100)