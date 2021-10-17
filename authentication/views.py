# Create your views here.
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required




def log_in(request):
    # Checking if the user is logged in
    # If so - redirect it to the page with the message list
    if request.user.is_authenticated:
        return redirect('/news')
    # Checking what type of HTTP request is
    # If POST user login attempt
    if request.method == 'POST':
        # Using the form to check if all data has been entered
        form = LoginForm(request.POST)
        if form.is_valid():
    # Using Django's built-in authentication system
    # to check if the user exists in the database
            user = authenticate(
            request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
            )
    # If the user exists - log him in
    # and redirect to news page
            if user is not None:
                login(request, user)
                return redirect('/news')
    # If it does not exist or the data sent is incomplete - send it
    # back to the customer with the data form
            else:
                context = {'form': form}
                return render(request, 'authentication/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authentication/login.html', context)
        # If GET is sending an empty form
    else:
        context = {'form': LoginForm()}
        return render(request, 'authentication/login.html', context)

@login_required(login_url='/login/')
def logout(request):
    django_logout(request)
    return redirect('/')