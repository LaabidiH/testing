from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class authentification(models.Model):
    nom_complet = models.CharField(max_length=100, null= True)
    email = models.EmailField(null= True)
    password = models.CharField(max_length=100 , null= True)
    poste_role = models.CharField(
        max_length=20,
        choices=[
            ("medecin", "medecin"),
            ("technicien", "technicien")
        ], 
        null= True
    )

class Personne(models.Model):
    nom_complet = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    tele = models.CharField(max_length=15)
    adresse = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    medecin = "medecin"
    technicien ="technicien"

    poste_role = models.CharField(
        max_length=20,
        choices=[
            (medecin, "medecin"),
            ("technicien", "technicien")
        ]
    )


    class Meta:
        abstract = True

class Medecin(Personne):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_medecin = models.CharField(
        max_length=20,
        choices=[
            ("medecine", "Medecine"),
            ("chirurgie", "Chirurgie"),
            ("pediaterie", "Pediaterie"),
            ("maternite", "Maternite")
        ]
    )
    inpe = models.CharField(max_length=10)
    responsable = models.BooleanField(default=False)

class PersonnelSoignant(Personne):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_role = models.CharField(
        max_length=20,
        choices=[
                ("SAA", "SAA")
            ]
    )

    # # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # SAA = "SAA"
    # medecine = "medecine"
    # chirurgie= "chirurgie"
    # centreDC="centreDC"
    # pediaterie = "pediaterie"
    # maternite = "maternite"
    # biologie = "biologie"
    # radiologie = "radiologie"

    # medecin = "medecin"
    # personnel_ ="personnel"

    # poste_role = [
    #     (medecin, "medecin"),
    #     (personnel_, "personnel")
    # ]

    # service_role = [
    #     (SAA, "SAA"),
    #     (medecine, "medecine"),
    #     (chirurgie, "chirurgie"),
    #     (centreDC, "centreDC"),
    #     (pediaterie,"pediaterie"),
    #     (maternite,"maternite"),
    #     (biologie,"biologie"),
    #     (radiologie,"radiologie")
    # ]
    # service_medecin = [
    #     (medecine, "medecine"),
    #     (chirurgie, "chirurgie"),
    #     (centreDC, "centreDC"),
    #     (pediaterie,"pediaterie"),
    #     (maternite,"maternite")
    # ]
    # nom = models.CharField(max_length=100)
    # username = models.CharField(max_length=100,unique=True)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)
    # tele = models.CharField(max_length=12)
    # INPE = models.CharField(max_length=20)
    # active = models.BooleanField(default=False)
    # adresse = models.CharField(max_length=128)
    # poste = models.CharField(
    #         max_length=20,
    #         choices=poste_role,
    #         default=SAA,
    #     )
    # roles = models.CharField(
    #     max_length=20,
    #     choices=service_role,
    #     default=SAA,
    # )
    # serviceMedecin = models.CharField(
    #     max_length=20,
    #     choices=service_medecin,
    #     null=True,
    # )

    # def __str__(self):
    #     return self.username    


def validate_file_extension(value):
    """
    Validation personnalisée pour les extensions de fichier autorisées.
    """
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.pdf']
    extension = str(value.name).lower().split('.')[-1]
    if extension not in allowed_extensions:
        raise ValidationError("Seules les extensions .jpg, .jpeg, .png et .pdf sont autorisées.")

class Consultation(models.Model):
    ipp = models.CharField(max_length=12)
    cin_assurant = models.CharField(max_length=12)
    ordonnance = models.FileField(upload_to='ordonnance/', validators=[validate_file_extension])
    date = models.DateField()

class Hospitalisation(Consultation):
    # Attributs spécifiques à l'hospitalisation
    dateSortie = models.CharField(max_length=100)
    billetHospitalisation = models.FileField(upload_to='billet_hosp/', validators=[validate_file_extension])
    facture = models.FileField(upload_to='facture/', validators=[validate_file_extension])

class Radio(Consultation):
    # Attributs spécifiques à la radio
    bonRadio = models.FileField(upload_to='bonRadio/', validators=[validate_file_extension])
    facture = models.FileField(upload_to='facture/', validators=[validate_file_extension])


class Biologie(Consultation):
    # Attributs spécifiques à la biologie
    bonBio = models.FileField(upload_to='bonBio/', validators=[validate_file_extension])
    facture = models.FileField(upload_to='facture/', validators=[validate_file_extension])


class DossierMedical(models.Model):
    consultations = models.ManyToManyField(Consultation)
    cinAssure = models.CharField(max_length=12)
    ipp = models.CharField(max_length=12)
    cnss = models.CharField(max_length=12)
    phCIN = models.FileField(upload_to='phCIN/', validators=[validate_file_extension])
    phCNSS = models.FileField(upload_to='phCNSS/', validators=[validate_file_extension])


