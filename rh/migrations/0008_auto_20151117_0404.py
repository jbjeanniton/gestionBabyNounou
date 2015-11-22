# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0007_auto_20151116_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='tel_principal',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond pas au format d'un numero de telephone", regex='^[0-9]{8}$')], verbose_name='No Telephone Principal'),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='tel_secondaire',
            field=models.CharField(max_length=20, blank=True, validators=[django.core.validators.RegexValidator(message="La valeur ne correspond pas au format d'un numero de telephone", regex='^[0-9]{8}$')], verbose_name='No Telephone Secondaire'),
        ),
    ]
