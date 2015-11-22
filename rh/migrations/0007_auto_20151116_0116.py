# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_zone'),
        ('rh', '0006_auto_20151115_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressourcehumaine',
            name='sexe',
            field=models.CharField(default='F', max_length=1, choices=[('F', 'F'), ('M', 'M')]),
        ),
        migrations.AddField(
            model_name='ressourcehumaine',
            name='zone',
            field=models.ForeignKey(null=True, to='base.Zone', blank=True),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='etat_matrimonial',
            field=models.CharField(verbose_name='Etat matrimonial', max_length=20, choices=[('celibataire', 'Celibataire'), ('marie', 'Marie(e)'), ('veuf', 'Veuf/Veuve'), ('divorce', 'Divorce(e)')]),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau',
            field=models.CharField(verbose_name="Niveau d'etude", max_length=20, choices=[('bac1', 'BAC I'), ('bac2', 'BAC II'), ('universitaire', 'Universitaire')]),
        ),
    ]
