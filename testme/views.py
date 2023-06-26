from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import *
import re


def Home(request):
    context = {}
    # Pour Medecin
    data = Medecin.objects.filter(active=False)
    return render(request,'techniciens_a.html', {'data':data})

def Home2(request):
    context = {}
    # Pour PersonnelSoignant
    data = PersonnelSoignant.objects.filter(active=False)
    return render(request,'index.html', {'data':data})


def actives(request):
    context = {}
    # Pour Medecin
    medecins_non_actifs = Medecin.objects.filter(active=True)

    # Pour PersonnelSoignant
    personnels_non_actifs = PersonnelSoignant.objects.filter(active=True)

    # Rassembler les objets eux-mêmes et les valeurs des champs dans une liste
    data = list(medecins_non_actifs) + list(personnels_non_actifs)
    return render(request,'comptes_actives.html', {'data':data})


def contact(request):
    context = {}
    return render(request,"contact.html")

def saa(request):
    context = {}
    return render(request,"saa.html")

def saa2(request):
    context = {}
    return render(request,"saa2.html")

def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

def validate_phone(phone):
    phone_regex = r'^(\+212|00212|0)(6|7)[0-9]{8}$'
    return re.match(phone_regex, phone)

def signup(request):
    poste = Personne._meta.get_field('poste_role').choices
    roles = PersonnelSoignant._meta.get_field('service_role').choices
    serviceMedecin = Medecin._meta.get_field('service_medecin').choices

    if request.method == 'POST':
        nom = request.POST['nom']
        password = request.POST['password']
        adresse = request.POST['adresse']
        email = request.POST['email']
        tele = request.POST['tele']
        service = request.POST['roles']
        service1 = request.POST['roles1'] 
        inpe= request.POST['inpe']
        poste = request.POST['poste']


        if not validate_email(email):
            error_message = "Format d'email non valide"
            return render(request, 'signup.html', {'roles': roles, 'error_message': error_message})
            
            # Valider le format du téléphone
        if not validate_phone(tele):
            error_message = "Format de téléphone non valide"
            return render(request, 'signup.html', {'roles': roles, 'error_message': error_message})
        
        if poste =="medecin":
            if nom and password and adresse and email and tele and service1:
                respo = request.POST['respo']
                if respo == "on":
                    respo = True
                else :
                    respo = False
                medecin = Medecin(
                    nom_complet=nom,
                    password=password,
                    adresse=adresse,
                    email=email,
                    tele=tele, 
                    inpe =inpe,
                    poste_role=poste,
                    service_medecin=service1,
                    responsable=respo
                )
                medecin.save()
                return redirect('login')
            else:
                error_message = "Tous les champs doivent être remplis"
                return render(request, 'signup.html', {'roles': roles, 'error_message': error_message,'poste':poste, 'serviceMedecin':serviceMedecin})

        
        if poste == "technicien" :
            if nom and password and adresse and email and tele and service:
                personnel = PersonnelSoignant(
                    nom_complet=nom,
                    password=password,
                    adresse=adresse,
                    email=email,
                    tele=tele, 
                    poste_role=poste,
                    service_role=service
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
        username = request.POST['email']
        password = request.POST['password']
        if authentification.objects.filter(email=username, password=password).exists():
            user = authentification.objects.filter(email=username, password=password).all()
            return redirect('home',{'context':user})
        else:
            pass
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     # L'authentification a réussi
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     # L'authentification a échoué
        #     error_message = "Nom d'utilisateur ou mot de passe incorrect."
        #     return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

