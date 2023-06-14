from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import *


def Home(request):

    context = {}
    data = Personnel.objects.filter(active = False)
    return render(request,'index.html', {'data':data})

def signup(request):
    roles = Personnel.service_role
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        adresse = request.POST['adresse']
        email = request.POST['email']
        tele = request.POST['tele']
        service = request.POST['roles']
        Personnel = Personnel(
            username=username,
            password=password,
            adresse=adresse,
            email=email,
            tele=tele, 
            roles=service
        )
        Personnel.save()
        return redirect('login')
    return render(request, 'signup.html', {'roles':roles})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # L'authentification a réussi
            login(request, user)
            return redirect('home')
        else:
            # L'authentification a échoué
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

