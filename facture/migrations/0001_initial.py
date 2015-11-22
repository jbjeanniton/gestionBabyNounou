# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0009_auto_20151116_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsFacture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nbr_enfant', models.PositiveSmallIntegerField(verbose_name='Nbr enfant', default=1)),
                ('nbr_jour_mensuel', models.PositiveSmallIntegerField(verbose_name='Nbr de jour / mois', default=26)),
                ('montant_prestation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('jour_absence', models.PositiveSmallIntegerField(default=0)),
                ('heure_supplementaire', models.PositiveSmallIntegerField(default=0)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(to='gestionclient.Contrat')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=11)),
                ('token', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(to='gestionclient.Client')),
            ],
        ),
        migrations.CreateModel(
            name='MoisFacture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('mois', models.CharField(max_length=7)),
                ('genere', models.BooleanField(default=False)),
                ('envoye', models.BooleanField(default=False)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=8)),
                ('devise', models.CharField(choices=[('USD', 'USD'), ('HTG', 'HTG')], max_length=3)),
                ('taux_du_jour', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('type', models.CharField(choices=[('Cash', 'Cash'), ('Chèque', 'Cheque'), ('Virement bancaire', 'Virement'), ('Carte de crédit', 'Carte de credit')], max_length=30)),
                ('no_transaction', models.CharField(max_length=32, blank=True)),
                ('date', models.DateField()),
                ('note', models.TextField(max_length=200, blank=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('facture', models.ForeignKey(to='facture.Facture')),
            ],
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=8)),
                ('devise', models.CharField(choices=[('USD', 'USD'), ('HTG', 'HTG')], max_length=3)),
                ('taux_du_jour', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('type', models.CharField(choices=[('Cash', 'Cash'), ('Chèque', 'Cheque'), ('Virement bancaire', 'Virement'), ('Carte de crédit', 'Carte de credit')], max_length=30)),
                ('no_transaction', models.CharField(max_length=32, blank=True)),
                ('date', models.DateField()),
                ('note', models.TextField(max_length=200, blank=True)),
                ('timestamp_add', models.DateTimeField(auto_now_add=True)),
                ('timestamp_update', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(to='gestionclient.Client')),
            ],
        ),
        migrations.AddField(
            model_name='facture',
            name='mois',
            field=models.ForeignKey(to='facture.MoisFacture'),
        ),
        migrations.AddField(
            model_name='detailsfacture',
            name='facture',
            field=models.ForeignKey(to='facture.Facture'),
        ),
    ]
