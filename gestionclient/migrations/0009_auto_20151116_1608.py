# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0008_auto_20151116_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_principal',
            field=models.EmailField(verbose_name='Email Principal', blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='email_secondaire',
            field=models.EmailField(verbose_name='Email Secondaire', blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='date_debut',
            field=models.DateField(null=True, verbose_name='Date de Début', blank=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='date_fin_prevue',
            field=models.DateField(null=True, verbose_name='Date de Fin', blank=True),
        ),
    ]
