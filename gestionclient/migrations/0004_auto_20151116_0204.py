# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0003_remove_enfant_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='date_naissance',
            field=models.DateField(verbose_name='Date de naissance', null=True, blank=True),
        ),
    ]
