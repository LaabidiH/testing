# Generated by Django 4.2.2 on 2023-06-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0026_authentification'),
    ]

    operations = [
        migrations.CreateModel(
            name='DossierPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ipp', models.IntegerField()),
                ('cin', models.CharField(max_length=20)),
            ],
        ),
    ]
