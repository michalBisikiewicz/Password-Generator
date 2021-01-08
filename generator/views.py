from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'home.html')


def password(request):
    characters = "abcdefghijklmnoprstuwxyz"
    uppercase = characters.upper()
    numbers = "1234567890"
    specials = "!@#$%^&*()"

    length = int(request.GET.get('length'))
    quantity = int(request.GET.get('quantity'))

    if request.GET.get('specials'):
        characters += specials

    if request.GET.get('uppercase'):
        characters += uppercase

    if request.GET.get('numbers'):
        characters += numbers

    lista = []

    for x in range(quantity):
        my_password = ''
        for char in range(length):
            my_password += random.choice(characters)
        lista.append(my_password)

    return render(request, 'generatedPassword.html', {'password': lista})


def about(request):
    return render(request, 'about.html')
