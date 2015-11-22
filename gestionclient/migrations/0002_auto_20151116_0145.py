# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientenfant',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientenfant',
            name='enfant',
        ),
        migrations.AddField(
            model_name='enfant',
            name='client',
            field=models.ForeignKey(null=True, to='gestionclient.Client', blank=True),
        ),
        migrations.DeleteModel(
            name='ClientEnfant',
        ),
    ]
