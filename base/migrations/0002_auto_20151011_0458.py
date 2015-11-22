# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='salaire_max',
            field=models.DecimalField(verbose_name='Salaire Maximum', decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='poste',
            name='salaire_min',
            field=models.DecimalField(verbose_name='Salaire Minimum', decimal_places=2, max_digits=8),
        ),
    ]
