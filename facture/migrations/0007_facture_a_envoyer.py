# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0006_auto_20151118_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='a_envoyer',
            field=models.BooleanField(default=True),
        ),
    ]
