# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0009_auto_20151119_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='ressourcehumaine',
            field=models.OneToOneField(verbose_name='Personne Ressource', to='rh.RessourceHumaine'),
        ),
        migrations.AlterField(
            model_name='nounou',
            name='est_mere',
            field=models.BooleanField(verbose_name='Est une mère'),
        ),
        migrations.AlterField(
            model_name='nounou',
            name='ressourcehumaine',
            field=models.OneToOneField(verbose_name='Personne Ressource', to='rh.RessourceHumaine'),
        ),
        migrations.AlterField(
            model_name='nounou',
            name='star',
            field=models.PositiveSmallIntegerField(verbose_name='Niveau', default=3),
        ),
    ]
