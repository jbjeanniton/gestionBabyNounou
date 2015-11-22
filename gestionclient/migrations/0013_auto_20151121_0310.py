# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151117_0404'),
        ('gestionclient', '0012_auto_20151120_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('deuxieme_prenom', models.CharField(blank=True, verbose_name='Deuxième prénom', max_length=100)),
                ('sexe', models.CharField(max_length=1, choices=[('F', 'F'), ('M', 'M')], default='F')),
                ('adresse', models.TextField(blank=True, max_length=300, null=True)),
                ('tel_principal', models.CharField(blank=True, verbose_name='No Telephone Principal', validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$', message="La valeur ne correspond pas au format d'un numero de telephone")], max_length=20)),
                ('tel_secondaire', models.CharField(blank=True, verbose_name='No Telephone Secondaire', validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$', message="La valeur ne correspond pas au format d'un numero de telephone")], max_length=20)),
                ('email_principal', models.EmailField(blank=True, verbose_name='Email Principal', max_length=254)),
                ('email_secondaire', models.EmailField(blank=True, verbose_name='Email Secondaire', max_length=254)),
                ('note', models.TextField(blank=True, max_length=200)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('zone', models.ForeignKey(blank=True, null=True, to='base.Zone')),
            ],
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': (('can_activate_client', 'Activer Client'),)},
        ),
        migrations.AlterField(
            model_name='client',
            name='adresse',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
