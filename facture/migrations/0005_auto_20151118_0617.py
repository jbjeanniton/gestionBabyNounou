# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151117_0404'),
        ('facture', '0004_auto_20151117_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailsfacture',
            name='contrat',
        ),
        migrations.AddField(
            model_name='detailsfacture',
            name='personalise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='detailsfacture',
            name='typeprestation',
            field=models.ForeignKey(to='base.TypePrestation', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facture',
            name='moisfacture',
            field=models.ForeignKey(to='facture.MoisFacture', verbose_name='mois'),
        ),
    ]
