# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151117_0404'),
        ('facture', '0002_versement_utilise'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsFactureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cout_option', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Cout Client (USD)')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('detailsfacture', models.ForeignKey(to='facture.DetailsFacture')),
                ('option', models.ForeignKey(to='base.Option')),
            ],
        ),
    ]
