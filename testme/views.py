from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import *
import re

####################
####################"
# #################
from io import BytesIO
from reportlab.pdfgen import canvas
from django.urls import reverse
from django.template.loader import get_template
from django.template import Context
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
from django.templatetags.static import static
from django.http import FileResponse

import PyPDF2
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


from .models import DossierPatient

from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def Home(request):
    context = {}
    # Pour Medecin
    medecins_non_actifs = Medecin.objects.filter(active=False)

    # Pour PersonnelSoignant
    personnels_non_actifs = PersonnelSoignant.objects.filter(active=False)

    # Rassembler les objets eux-mêmes et les valeurs des champs dans une liste
    data = list(medecins_non_actifs) + list(personnels_non_actifs)

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

#############################
##############################"
# #######################"#####"

def home_M(request):
    return render(request , 'home_M.html')

def scan_M(request):
    return render(request , 'scan_M.html')

def prischarge(request):
    return render(request, 'prischarge.html')   

def contact_M(request):
    return render(request, 'contact_M.html') 
def archive_P(request):
    return render(request, 'archive_P.html') 
def archive_CH(request):
    return render(request, 'archive_CH.html') 

header_image = "testme/static/img/header.png"
footer_image = "testme/static/img/footer.png"
#generate pdf pli confidentiel
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from django.http import HttpResponse

def generate_pdf(request):
    # Retrieve form data
    nom_prenom = request.POST.get('NomPrenom')
    date_entree = request.POST.get('DateEntree')
    date_sortie = request.POST.get('DateSortie')
    admission = request.POST.get('Admission')
    service = request.POST.get('Service')
    motif_hospitalisation = request.POST.get('Motif')
    compte_rendu_hospitalisation = request.POST.get('CompteRendu')
    compte_rendu_operatoire = request.POST.get('CompteOperatoire')

    # Create a BytesIO buffer to store the PDF content
    buffer = BytesIO()

    # Create the PDF object
    p = canvas.Canvas(buffer, pagesize=letter)

    # Set the font and font size for the header and footer
    p.setFont("Helvetica-Bold", 12)
    # Split the text into lines based on the line width
    text = f"Objet: PI Confidentiel"
    text_width = pdfmetrics.stringWidth(text, "Helvetica", 14)
    center_x = (letter[0] - text_width) / 2

    # Load and draw the header image
    header_image = "testme/static/img/header.png"  # Replace with your own image file
    header_width = 4.5 * inch
    header_height = 1.0 * inch
    header_x = 150
    header_y = 700
    p.drawImage(header_image, header_x, header_y, width=header_width, height=header_height)

    # Load and draw the footer image
    footer_image = "testme/static/img/footer.png"  # Replace with your own image file
    footer_width = 2.5 * inch
    footer_height = 0.5 * inch
    footer_x = 200
    footer_y = 20
    p.drawImage(footer_image, footer_x, footer_y, width=footer_width, height=footer_height)

    # Write the form data to the PDF body
    body_x = 100
    body_y = 600

# Write the form data to the PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, 600, f"Nom et prénom du patient: {nom_prenom}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 580, f"Date d'entrée: {date_entree}")
    p.drawString(300, 580, f"Date de sortie: {date_sortie}")
    p.drawString(100, 560, f"N°d'Admission: {admission}")
    p.drawString(300, 560, f"Service: {service}")
    p.setFont("Helvetica", 12)
    p.drawString(center_x, 520, text)
    p.drawString(100, 500, f"Motif d'hospitalisation: {motif_hospitalisation}")
    p.drawString(100, 400, f"Compte rendu d'hospitalisation : {compte_rendu_hospitalisation}")
    p.drawString(100, 350, f"Compte rendu Opératoire: {compte_rendu_operatoire}")
    p.setFont("Helvetica", 10)
    p.drawString(400, 300, f"Signature et cachet du mdecin")

    # Save the PDF
    p.showPage()
    p.save()

    # Set the filename of the generated PDF with the patient's name
    filename = f"{nom_prenom}_fichier.pdf"

    # Create the HTTP response with the PDF content
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response



def liste_dossiers_patients(request):
    dossiers = DossierPatient.objects.all()
    return render(request, 'testme/liste_dossiers_patients.html', {'dossiers': dossiers})



def generate_pdf_pris(request):
    if request.method == 'POST':
        immatriculation = request.POST.get('immatriculation', '')
        nomPrenomAssure = request.POST.get('nomPrenomAssure', '')

        # Data for the table
        data = [
            ["Frals de séjour", "Séjour normal", "Solns intensils", "Réanimation", "Couveuse"],
            ["Nbre jours", "", "", "", ""],
            ["Tarif unitaire", "", "", "", ""],
            ["Total", "", "", "", ""],
        ]
        style = TableStyle([
            ("BACKGROUND", (0, 0), (0, 3), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Create the PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Create the table
        table = Table(data)

        # Apply the style to the table
        table.setStyle(style)

        # Build the story and add the table
        story = []
        story.append(table)
        doc.build(story)

        return response

    return render(request, 'prischarge.html')
