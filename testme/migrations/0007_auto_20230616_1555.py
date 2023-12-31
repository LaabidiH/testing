# Generated by Django 3.2.19 on 2023-06-16 13:55

from django.db import migrations, models
import django.db.models.deletion
import testme.models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0006_alter_personnel_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin_assurant', models.CharField(max_length=12)),
                ('ordonnance', models.FileField(upload_to='ordonnance/', validators=[testme.models.validate_file_extension])),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='poste',
            field=models.CharField(choices=[('medecin', 'medecin'), ('personnel', 'personnel')], default='personnel', max_length=20),
        ),
        migrations.CreateModel(
            name='Biologie',
            fields=[
                ('consultation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testme.consultation')),
                ('bonBio', models.FileField(upload_to='bonBio/', validators=[testme.models.validate_file_extension])),
            ],
            bases=('testme.consultation',),
        ),
        migrations.CreateModel(
            name='Hospitalisation',
            fields=[
                ('consultation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testme.consultation')),
                ('dateSortie', models.CharField(max_length=100)),
                ('billetHospitalisation', models.FileField(upload_to='billet_hosp/', validators=[testme.models.validate_file_extension])),
                ('facture', models.FileField(upload_to='facture/', validators=[testme.models.validate_file_extension])),
            ],
            bases=('testme.consultation',),
        ),
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('consultation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testme.consultation')),
                ('bonRadio', models.FileField(upload_to='bonRadio/', validators=[testme.models.validate_file_extension])),
            ],
            bases=('testme.consultation',),
        ),
        migrations.CreateModel(
            name='DossierMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinAssure', models.CharField(max_length=12)),
                ('ipp', models.CharField(max_length=12)),
                ('cnss', models.CharField(max_length=12)),
                ('phCIN', models.FileField(upload_to='phCIN/', validators=[testme.models.validate_file_extension])),
                ('phCNSS', models.FileField(upload_to='phCNSS/', validators=[testme.models.validate_file_extension])),
                ('consultations', models.ManyToManyField(to='testme.Consultation')),
            ],
        ),
    ]
