# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0002_auto_20151012_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='date_fin',
            field=models.DateField(verbose_name='Date de fin', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='salaire',
            field=models.DecimalField(max_digits=8, verbose_name='Salaire Brut', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='nounou',
            name='date_fin',
            field=models.DateField(verbose_name='Date de fin', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau_anglais',
            field=models.PositiveSmallIntegerField(verbose_name='Niveau anglais', blank=True, choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')], null=True),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='niveau_francais',
            field=models.PositiveSmallIntegerField(verbose_name='Niveau francais', blank=True, choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')], null=True),
        ),
    ]
