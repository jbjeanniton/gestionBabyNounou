# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom du Poste')),
                ('description', models.TextField(max_length=100, blank=True, verbose_name='Description')),
                ('salaire_min', models.DecimalField(decimal_places=2, verbose_name='Salaire Minimum', max_digits=6)),
                ('salaire_max', models.DecimalField(decimal_places=2, verbose_name='Salaire Maximum', max_digits=6)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePrestation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom de la Prestation')),
                ('horaire', models.TextField(max_length=200, verbose_name='Horaire Prevu')),
                ('prix_base', models.TextField(max_length=100, blank=True, verbose_name='Prix de Base')),
                ('prix_double', models.TextField(max_length=100, blank=True, verbose_name='Prix pour 2 enfants')),
                ('actif', models.TextField(max_length=100, blank=True, verbose_name='Actif')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
