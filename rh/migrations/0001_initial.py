# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151012_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('libre', models.BooleanField(verbose_name='Libre')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_debut', models.DateField(verbose_name='Date de debut')),
                ('date_fin', models.DateField(verbose_name='Date de fin', blank=True)),
                ('salaire', models.DecimalField(max_digits=8, verbose_name='Salaire reelle', decimal_places=2)),
                ('note', models.TextField(verbose_name='Note', max_length=200, blank=True)),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('poste', models.ForeignKey(to='base.Poste')),
            ],
        ),
        migrations.CreateModel(
            name='Nounou',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_debut', models.DateField(verbose_name='Date de debut')),
                ('date_fin', models.DateField(verbose_name='Date de fin', blank=True)),
                ('star', models.TextField(verbose_name='Description', max_length=100, blank=True)),
                ('est_mere', models.BooleanField(verbose_name='Est une mere')),
                ('note', models.TextField(verbose_name='Note', max_length=200, blank=True)),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NounouOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nounou', models.ForeignKey(to='rh.Nounou')),
                ('option', models.ForeignKey(to='base.Option')),
            ],
        ),
        migrations.CreateModel(
            name='RessourceHumaine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('deuxieme_prenom', models.CharField(verbose_name='Deuxième prénom', max_length=100, blank=True)),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=100, verbose_name='Lieu de naissance')),
                ('no_id', models.CharField(max_length=20, verbose_name='ID/CIN')),
                ('nom_mere', models.CharField(verbose_name='Nom de la mere', max_length=100, blank=True)),
                ('etat_matrimonial', models.CharField(max_length=100, verbose_name='Etat matrimonial', choices=[('celibataire', 'Celibataire'), ('marie', 'Marie(e)'), ('veuf', 'Veuf/Veuve'), ('divorce', 'Divorce(e)')])),
                ('religion', models.CharField(verbose_name='Religion', max_length=100, blank=True)),
                ('nbr_enfant_charge', models.PositiveSmallIntegerField(verbose_name='Nbr enfant a charge', default=0)),
                ('adresse', models.TextField(max_length=300, verbose_name='Adresse')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville')),
                ('tel', models.CharField(max_length=20, verbose_name='Telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('niveau', models.CharField(max_length=100, verbose_name="Niveau d'etude")),
                ('formation', models.TextField(verbose_name='Formation', max_length=100, blank=True)),
                ('niveau_francais', models.CharField(verbose_name='Niveau francais', max_length=100, blank=True, choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')])),
                ('niveau_anglais', models.CharField(verbose_name='Niveau anglais', max_length=100, blank=True, choices=[(1, 'Debutant'), (2, 'Elementaire'), (3, 'Intermediaire'), (4, 'Avance')])),
                ('note', models.TextField(verbose_name='Note', max_length=200, blank=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='nounou',
            name='ressourcehumaine',
            field=models.OneToOneField(to='rh.RessourceHumaine'),
        ),
        migrations.AddField(
            model_name='employe',
            name='ressourcehumaine',
            field=models.OneToOneField(to='rh.RessourceHumaine'),
        ),
        migrations.AddField(
            model_name='disponibilite',
            name='nounou',
            field=models.ForeignKey(to='rh.Nounou'),
        ),
        migrations.AddField(
            model_name='disponibilite',
            name='typeprestation',
            field=models.ForeignKey(to='base.TypePrestation'),
        ),
    ]
