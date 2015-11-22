# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0009_auto_20151119_0345'),
        ('facture', '0008_auto_20151120_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsfacture',
            name='nounou',
            field=models.ForeignKey(to='rh.Nounou', null=True, blank=True),
        ),
    ]
