# Generated by Django 3.2.19 on 2023-06-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0014_alter_personnel_servicemedecin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='serviceMedecin',
            field=models.CharField(choices=[('medecine', 'medecine'), ('chirurgie', 'chirurgie'), ('centreDC', 'centreDC'), ('pediaterie', 'pediaterie'), ('maternite', 'maternite')], max_length=20, null=True),
        ),
    ]
