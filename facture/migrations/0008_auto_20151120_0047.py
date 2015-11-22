# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0007_facture_a_envoyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0),
        ),
        migrations.AlterField(
            model_name='facture',
            name='a_envoyer',
            field=models.BooleanField(verbose_name='Envoi par mail', default=True),
        ),
        migrations.AlterField(
            model_name='facture',
            name='code',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
