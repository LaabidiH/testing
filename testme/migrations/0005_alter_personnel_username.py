# Generated by Django 3.2.19 on 2023-06-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0004_alter_personnel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='username',
            field=models.CharField(default='Fato', max_length=100, unique=True),
        ),
    ]
