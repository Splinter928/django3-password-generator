from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def description(request):
    return render(request, 'generator/description.html')


def password(request):
    chars = list("abcdefghijkmnpqrstuvwxyz")

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list(r'!\"#$%&()*+,-./:;<=>?@[\]^_{|}~'))

    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(chars)

    return render(request, 'generator/password.html', {'password': thepassword})
