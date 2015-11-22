# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0011_contrat_nounou'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': (('can_activate_client', 'Can deliver pizzas'),)},
        ),
    ]
