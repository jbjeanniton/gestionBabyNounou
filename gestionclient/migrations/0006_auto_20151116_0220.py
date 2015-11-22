# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0005_auto_20151116_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='ville',
        ),
        migrations.AlterField(
            model_name='client',
            name='email_principal',
            field=models.EmailField(max_length=254, blank=True, verbose_name='Email'),
        ),
    ]
