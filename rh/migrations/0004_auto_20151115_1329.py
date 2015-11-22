# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0003_auto_20151012_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressourcehumaine',
            name='niveau_espagnol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')], blank=True, verbose_name='Niveau Espagnol', null=True),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='no_id',
            field=models.CharField(max_length=20, unique=True, verbose_name='ID/CIN'),
        ),
    ]
