# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeprestation',
            name='prix_base',
        ),
        migrations.RemoveField(
            model_name='typeprestation',
            name='prix_double',
        ),
        migrations.AddField(
            model_name='typeprestation',
            name='prix_base_client',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, verbose_name='Prix de base (USD) | Client', max_digits=8),
        ),
        migrations.AddField(
            model_name='typeprestation',
            name='prix_base_nounou',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, verbose_name='Prix de base (HTG) | Nounou', max_digits=8),
        ),
        migrations.AddField(
            model_name='typeprestation',
            name='prix_double_client',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, verbose_name='Prix pour 2 enfants (USD) | Client', max_digits=8),
        ),
        migrations.AddField(
            model_name='typeprestation',
            name='prix_double_nounou',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, verbose_name='Prix pour 2 enfants (HTG) | Nounou', max_digits=8),
        ),
    ]
