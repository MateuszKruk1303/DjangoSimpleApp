from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import News
from .forms import NewsForm, NewsEditForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def view_news(request):
    # Get data from DB
    news = News.objects.order_by('-create_time')
    # Create a dictionary containing the db entries
    # in a variable called news
    context = {'news': news}
    # Send the rendered site with
    # DB data
    # elements from the context dictionary
    # are used in news/index.html
    return render(request, 'news/index.html', context)

@login_required(login_url='/login/')
def add(request):
    #Checking the method of the HTTP request
    # If POST - we are looking for data in the body of the query
    # If GET - send the form to be filled in
    # (you can send data in the GET query -
    # but in this solution we do not use it)
    if request.method == 'POST':
    # Forms in Django allow you to validate data
    # so we create the form object from the query
        news = NewsForm(request.POST)
    # If the form - i.e. data sent from the POST query
    # are correct add an element to the database
        if news.is_valid():
            news = news.save(commit=False)
            # news.author = request.user
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('/news') #Zmiana - widok -> url
    # If they are not correct, we send the form back to the client
    # The automatic validator also creates error fields that are,→accessible from
    # the client side
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    # If a GET query is sent an empty form
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)



def get(request, id):
    # function get_object_or_404 returns an element from the database
    # data with a given argument value
    # or sends an error to the client
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/view.html', context)

@login_required(login_url='/login/')
def delete(request, topic):
    model = News
    model.objects.filter(topic=topic).delete()
    return redirect('/news/')

@login_required(login_url='/login/')        
def edit_title(request, topic):
    model = News
    news_form = NewsEditForm(request.POST)
    obj = model.objects.get(topic=topic)
    obj.topic = news_form.data.get("new_topic", "0")
    obj.save()
    return redirect('/news/')
