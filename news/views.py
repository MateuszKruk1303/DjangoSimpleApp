from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def view_news(request):
    return HttpResponse("News")