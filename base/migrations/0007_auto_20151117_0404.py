# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151116_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_base_client',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=8, verbose_name='Prix Client (USD)'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_base_nounou',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=8, verbose_name='Prix Nounou (HTG)'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_double_client',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=8, verbose_name='Prix Client (USD)'),
        ),
        migrations.AlterField(
            model_name='typeprestation',
            name='prix_double_nounou',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=8, verbose_name='Prix Nounou (HTG)'),
        ),
    ]
