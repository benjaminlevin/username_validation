from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Message
from datetime import datetime


def index(request):
    context = {
        "message" : Message.objects.all(),
    }
    return render(request, "unvalid/index.html", context)

def validate(request):
    Message.objects.all().delete()
    username = request.POST['username']
    check = User.objects.filter(username=username)
    if check.exists():
        Message.objects.create(message="Username already entered!")
        return redirect('/')
    elif len(username) < 26 and len(username) >8:
        print username
        User.objects.create(username=request.POST['username'])
        Message.objects.create(message="The username you entered ("+username+") is valid. Thank you!")
        return redirect('/success')
    else:
        Message.objects.create(message="Username is not valid!")
        return redirect('/')

def success(request):
    context = {
        "message" : Message.objects.all(),
        "user" : User.objects.all(),
        #"created_at" : User.objects.all(created_at=created_at).strftime('%-I:%M %p')
    }
    return render(request, "unvalid/success.html", context)

def delete(request, id):
    User.objects.filter(id=id).delete()
    return redirect('/success')

def reset(request):
    Message.objects.all().delete()
    return redirect('/')
