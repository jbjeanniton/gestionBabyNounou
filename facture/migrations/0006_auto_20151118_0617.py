# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0005_auto_20151118_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsfacture',
            name='typeprestation',
            field=models.ForeignKey(to='base.TypePrestation', blank=True, null=True),
        ),
    ]
