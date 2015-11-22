# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ('gestionclient', '0006_auto_20151116_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tel_principal',
            field=models.CharField(verbose_name='No Telephone Principal', validators=[
                django.core.validators.RegexValidator(regex='^509[0-9]{8}$',
                                                      message="La valeur ne correspond pas au format d'un numero de telephone")],
                                   blank=True, max_length=20),
        ),
    ]
