# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151117_0404'),
        ('gestionclient', '0009_auto_20151116_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(to='gestionclient.Contrat')),
                ('option', models.ForeignKey(to='base.Option')),
            ],
        ),
    ]
