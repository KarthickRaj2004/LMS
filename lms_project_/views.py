# views.py

from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')

