# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0005_auto_20151115_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='tel_principal',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond pas au format d'un numero de telephone", regex='^509[0-9]{8}$')], verbose_name='No Telephone Principal'),
        ),
    ]
