from django.db import models

from django.db import models

class Personnel(models.Model):
    SAA = "SAA"
    medecin = "medecin"

    service_role = [
        (SAA, "SAA"),
        (medecin, "medecin"),
    ]
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    tele = models.CharField(max_length=12)
    active = models.BooleanField(default=False)
    adresse = models.CharField(max_length=128)
    roles = models.CharField(
        max_length=20,
        choices=service_role,
        default=SAA,
    )

    def __str__(self):
        return self.username    
