from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import *
import re


def Home(request):
    context = {}
    data = Personnel.objects.filter(active = False)
    return render(request,'index.html', {'data':data})

def actives(request):
    context = {}
    data = Personnel.objects.filter(active = True)
    return render(request,'comptes_actives.html', {'data':data})

def contact(request):
    context = {}
    return render(request,"contact.html")


def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

def validate_phone(phone):
    phone_regex = r'^(\+212|00212|0)(6|7)[0-9]{8}$'
    return re.match(phone_regex, phone)

def signup(request):
    roles = Personnel.service_role  # Utiliser les choix définis dans le modèle Personnel
    poste = Personnel.poste_role
    serviceMedecin = Personnel.service_medecin
    if request.method == 'POST':
        nom = request.POST['nom']
        username = request.POST['username']
        password = request.POST['password']
        adresse = request.POST['adresse']
        email = request.POST['email']
        tele = request.POST['tele']
        service = request.POST['roles']
        service1 = request.POST['roles1'] 
        inpe= request.POST['inpe']
        poste = request.POST['poste']

        if service=="SAA" and poste =="medecin":
            service = service1
        
        if poste == "personnel" :
            service1 = None
        # Vérifier si les champs sont bien remplis
        if nom and username and password and adresse and email and tele and service:
            # Valider le format de l'email
            if not validate_email(email):
                error_message = "Format d'email non valide"
                return render(request, 'signup.html', {'roles': roles, 'error_message': error_message})
            
            # Valider le format du téléphone
            if not validate_phone(tele):
                error_message = "Format de téléphone non valide"
                return render(request, 'signup.html', {'roles': roles, 'error_message': error_message})
            
            personnel = Personnel(
                nom=nom,
                username=username,
                password=password,
                adresse=adresse,
                email=email,
                tele=tele, 
                roles=service,
                poste=poste,
                INPE =inpe,
                serviceMedecin=service1
            )
            personnel.save()
            return redirect('login')
        else:
            error_message = "Tous les champs doivent être remplis"
            return render(request, 'signup.html', {'roles': roles, 'error_message': error_message,'poste':poste, 'serviceMedecin':serviceMedecin})
    
    return render(request, 'signup.html', {'roles':roles,'poste':poste,'serviceMedecin':serviceMedecin})

def archive_dossiers(request):
    context = {}
    data = Hospitalisation.objects.filter()
    return render(request,"archive_dossiers.html", {'data':data})

def service_biologie(request):
    context = {}
    data = Hospitalisation.objects.filter()
    return render(request,"service_biologie.html", {'data':data})

def service_radio(request):
    context = {}
    data = Hospitalisation.objects.filter()
    return render(request,"service_radio.html", {'data':data})

def service_radioL(request):
    context = {}
    data = Hospitalisation.objects.filter()
    return render(request,"service_radioL.html", {'data':data})

def service_biologieL(request):
    context = {}
    data = Hospitalisation.objects.filter()
    return render(request,"service_biologieL.html", {'data':data})

def cons(request):
    data = Consultation.objects.filter()
    return render(request,'dossiers_consultation.html', {'data':data})

def radio(request):
    data = Radio.objects.filter()
    return render(request,'radio_dossiers.html', {'data':data})

def bio(request):
    data = Biologie.objects.filter()
    return render(request,'bio_dossiers.html', {'data':data})

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

