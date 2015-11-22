# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151011_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeprestation',
            name='actif',
            field=models.BooleanField(verbose_name='Actif'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_base',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Prix de Base'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_double',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Prix pour 2 enfants'),
        ),
    ]
