# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0008_auto_20151117_0404'),
        ('gestionclient', '0010_contratoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='nounou',
            field=models.ForeignKey(null=True, to='rh.Nounou', blank=True),
        ),
    ]
