from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Message
from datetime import datetime


def index(request):
    # This function represents login into the chat
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('room'))
        else:
            print(form.errors)
    return render(request, 'index.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('index'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors)
    return render(request, 'sign_up.html', {'form': form})


def room(request):
    nickname = str(request.user)
    return render(request, 'room.html', {'nickname': nickname})


def get_data_from_js(request):
    # This function obtains chat inputs from frontend script and records them into postrgres db
    text = request.GET.get('message')
    author_nickname = request.GET.get('author')
    author = User.objects.get(username=author_nickname)
    Message.objects.create(text=text, author=author, time_sent=datetime.now())
    return render(request, 'room.html', {'nickname': str(request.user)})
