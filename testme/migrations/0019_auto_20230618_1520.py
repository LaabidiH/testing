# Generated by Django 3.2.19 on 2023-06-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0018_auto_20230618_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personnelsoignant',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
