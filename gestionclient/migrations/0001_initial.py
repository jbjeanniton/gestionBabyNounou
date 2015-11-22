# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0005_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(verbose_name='Nom', max_length=100)),
                ('prenom', models.CharField(verbose_name='Prénom', max_length=100)),
                ('deuxieme_prenom', models.CharField(blank=True, verbose_name='Deuxième prénom', max_length=100)),
                ('sexe', models.CharField(choices=[('F', 'F'), ('M', 'M')], default='F', max_length=1)),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(verbose_name='Lieu de naissance', max_length=100)),
                ('no_id', models.CharField(validators=[django.core.validators.RegexValidator(
                    regex='^[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{1}$|^\\d{2}-\\d{2}-\\d{2}-\\d{4}-\\d{2}-\\d{5}$',
                    message="La valeur ne correspond ni au formt d'un code CIN ni a celui d'un NIF")],
                    verbose_name='ID/CIN', unique=True, max_length=20)),
                ('adresse', models.TextField(max_length=300)),
                ('ville', models.CharField(verbose_name='Ville', max_length=100)),
                ('tel_principal', models.CharField(validators=[
                    django.core.validators.RegexValidator(regex='^509[0-9]{8}$',
                                                          message="La valeur ne correspond pas au format d'un numero de telephone")],
                    verbose_name='No Telephone Principal', max_length=20)),
                ('tel_secondaire', models.CharField(blank=True, validators=[
                    django.core.validators.RegexValidator(regex='^509[0-9]{8}$',
                                                          message="La valeur ne correspond pas au format d'un numero de telephone")],
                                                    verbose_name='No Telephone Secondaire', max_length=20)),
                ('email_principal', models.EmailField(verbose_name='Email', max_length=254)),
                ('email_secondaire', models.EmailField(blank=True, verbose_name='Email', max_length=254)),
                ('note', models.TextField(blank=True, max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('zone', models.ForeignKey(null=True, blank=True, to='base.Zone')),
            ],
        ),
        migrations.CreateModel(
            name='ClientEnfant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(to='gestionclient.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('personalise', models.BooleanField(default=False)),
                ('nbr_enfant', models.PositiveSmallIntegerField(verbose_name='Nbr enfant', default=1)),
                ('nbr_jour_mensuel', models.PositiveSmallIntegerField(verbose_name='Nbr de jour / mois', default=26)),
                ('montant_prestation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_debut', models.DateField(verbose_name='Date de Début')),
                ('date_fin_prevue', models.DateField(verbose_name='Date de Fin')),
                ('date_fin_reel', models.DateField(null=True, blank=True, verbose_name='Date de Fin Réel')),
                ('actif', models.BooleanField(default=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(to='gestionclient.Client')),
                ('typeprestation', models.ForeignKey(to='base.TypePrestation')),
            ],
        ),
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nom', models.CharField(verbose_name='Nom', max_length=100)),
                ('prenom', models.CharField(verbose_name='Prénom', max_length=100)),
                ('deuxieme_prenom', models.CharField(blank=True, verbose_name='Deuxième prénom', max_length=100)),
                ('sexe', models.CharField(choices=[('F', 'F'), ('M', 'M')], default='F', max_length=1)),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('note', models.TextField(blank=True, max_length=200)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='clientenfant',
            name='enfant',
            field=models.ForeignKey(to='gestionclient.Enfant'),
        ),
    ]
