from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    return render(request, 'register.html')
    
def registration_success(request):
    return render(request, 'registration_success.html')

""" 
def index(reuest):
    user = models.User.username
    password = models.User.password
    high_score = models.User.high_score
    
    context = {
        'password':password,
        'user':user,
        'high_score':high_score
    }
    
    return render(request, 'index.html', context)
    
"""
