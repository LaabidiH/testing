# Generated by Django 3.2.19 on 2023-06-19 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0020_auto_20230619_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='username',
        ),
        migrations.RemoveField(
            model_name='personnelsoignant',
            name='username',
        ),
    ]