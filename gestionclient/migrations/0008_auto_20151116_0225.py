# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ('gestionclient', '0007_auto_20151116_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='no_id',
            field=models.CharField(verbose_name='ID/CIN', blank=True, max_length=20, validators=[
                django.core.validators.RegexValidator(
                    regex='^[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{1}$|^\\d{2}-\\d{2}-\\d{2}-\\d{4}-\\d{2}-\\d{5}$',
                    message="La valeur ne correspond ni au formt d'un code CIN ni a celui d'un NIF")], null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='tel_principal',
            field=models.CharField(verbose_name='No Telephone Principal', blank=True, max_length=20, validators=[
                django.core.validators.RegexValidator(regex='^[0-9]{8}$',
                                                      message="La valeur ne correspond pas au format d'un numero de telephone")]),
        ),
        migrations.AlterField(
            model_name='client',
            name='tel_secondaire',
            field=models.CharField(verbose_name='No Telephone Secondaire', blank=True, max_length=20, validators=[
                django.core.validators.RegexValidator(regex='^[0-9]{8}$',
                                                      message="La valeur ne correspond pas au format d'un numero de telephone")]),
        ),
    ]
