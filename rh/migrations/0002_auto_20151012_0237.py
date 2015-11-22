# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau',
            field=models.CharField(verbose_name="Niveau d'etude", choices=[('bac1', 'BAC I'), ('bac2', 'BAC II'), ('universitaire', 'Universitaire')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau_anglais',
            field=models.PositiveSmallIntegerField(verbose_name='Niveau anglais', choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')], blank=True),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau_francais',
            field=models.PositiveSmallIntegerField(verbose_name='Niveau francais', choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')], blank=True),
        ),
    ]
