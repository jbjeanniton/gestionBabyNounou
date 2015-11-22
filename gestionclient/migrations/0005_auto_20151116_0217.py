# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0004_auto_20151116_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_naissance',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lieu_naissance',
        ),
    ]
