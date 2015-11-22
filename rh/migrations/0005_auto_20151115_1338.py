# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0004_auto_20151115_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ressourcehumaine',
            name='tel',
        ),
        migrations.AddField(
            model_name='ressourcehumaine',
            name='tel_principal',
            field=models.CharField(verbose_name='No Telephone Principal', blank=True, validators=[django.core.validators.RegexValidator(regex='^509[0-9]{8}$', message="La valeur ne correspond pas au format d'un numero de telephone")], max_length=20),
        ),
        migrations.AddField(
            model_name='ressourcehumaine',
            name='tel_secondaire',
            field=models.CharField(verbose_name='No Telephone Secondaire', blank=True, validators=[django.core.validators.RegexValidator(regex='^509[0-9]{8}$', message="La valeur ne correspond pas au format d'un numero de telephone")], max_length=20),
        ),
        migrations.AlterField(
            model_name='ressourcehumaine',
            name='no_id',
            field=models.CharField(verbose_name='ID/CIN', unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{1}$|^\\d{2}-\\d{2}-\\d{2}-\\d{4}-\\d{2}-\\d{5}$', message="La valeur ne correspond ni au formt d'un code CIN ni a celui d'un NIF")], max_length=20),
        ),
    ]
