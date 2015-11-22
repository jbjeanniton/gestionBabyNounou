# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151012_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name='Description', blank=True, max_length=200)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('type', models.CharField(choices=[('departement', 'Département'), ('commune', 'Commune'),
                                                   ('section_communale', 'Section Communale')], max_length=20)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
