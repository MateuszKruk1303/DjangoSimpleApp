from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['topic', 'text', 'author']
        # topic = forms.CharField(label='Topic', max_length=100)
        # text = forms.CharField(label='Text', max_length=100)
        # author = forms.CharField(label='Author', max_length=100)

class NewsEditForm(forms.Form):
    new_topic = forms.CharField(label='New topic', max_length=100)