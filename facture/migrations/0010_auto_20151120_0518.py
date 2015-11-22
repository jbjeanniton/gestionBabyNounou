# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0009_detailsfacture_nounou'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facture',
            options={'permissions': (('can_generate_facture', 'Générer Factures'), ('can_send_facture', 'Envoyer Factures'))},
        ),
    ]
