# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0008_auto_20151117_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressourcehumaine',
            name='no_compte',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='ressourcehumaine',
            name='nom_banque',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='ressourcehumaine',
            name='nom_compte',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
