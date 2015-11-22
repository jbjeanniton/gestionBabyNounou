# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151011_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Type Option')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Description')),
                ('cout_client', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cout Client (USD)')),
                ('cout_nounou', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cout Nounou (HTG)')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('actif', models.BooleanField(verbose_name='Actif')),
            ],
        ),
        migrations.AlterField(
            model_name='poste',
            name='salaire_max',
            field=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Salaire Maximum (HTG)'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='salaire_min',
            field=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Salaire Minimum (HTG)'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_base',
            field=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Prix de base (USD)'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_double',
            field=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Prix pour 2 enfants (USD)'),
        ),
    ]
