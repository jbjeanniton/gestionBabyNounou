# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0003_detailsfactureoption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facture',
            old_name='mois',
            new_name='moisfacture',
        ),
        migrations.AlterField(
            model_name='facture',
            name='token',
            field=models.CharField(max_length=50),
        ),
    ]
