from django.db import models
from gestionBabyNounou.common_lst  import *


# Create your models here.

class Zone(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, verbose_name="Description")
    code = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=20, choices=NIVEAU_ZONE)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class Poste(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du Poste")
    description = models.TextField(max_length=100, blank=True, verbose_name="Description")
    salaire_min = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salaire Minimum (HTG)")
    salaire_max = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salaire Maximum (HTG)")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom


class TypePrestation(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de la Prestation")
    horaire = models.TextField(max_length=200, verbose_name="Horaire Prevu")
    prix_base_client = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix Client (USD)", blank=True, null=True)
    prix_double_client = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix Client (USD)", blank=True, null=True)
    prix_base_nounou = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix Nounou (HTG)", blank=True, null=True)
    prix_double_nounou= models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix Nounou (HTG)", blank=True, null=True)
    actif = models.BooleanField(verbose_name="Actif")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def prix_de_base(self):  # __unicode__ on Python 2
        prix_client = '--' if not self.prix_base_client else "<span style='display: inline-block; width: 130px; padding: 2px;'>Coût de la prestation : </span><strong style='display: inline-block; width: 100px; text-align: right'>USD %s</strong><br>" % (self.prix_base_client)
        prix_nounou = '--' if not self.prix_base_nounou else "<span style='display: inline-block; width: 130px; padding: 2px;'>Salaire de la nounou : </span><strong style='display: inline-block; width: 100px; text-align: right'>HTG %s</strong>" % (self.prix_base_nounou)
        return "%s %s" % (prix_client, prix_nounou)
    prix_de_base.allow_tags = True

    def prix_pour_2_enfants(self):  # __unicode__ on Python 2
        prix_client = '--' if not self.prix_double_client else "<span style='display: inline-block; width: 130px; padding: 2px;'>Coût de la prestation : </span><strong style='display: inline-block; width: 100px; text-align: right'>USD %s</strong><br>" % (self.prix_double_client)
        prix_nounou = '--' if not self.prix_double_nounou else "<span style='display: inline-block; width: 130px; padding: 2px;'>Salaire de la nounou : </span><strong style='display: inline-block; width: 100px; text-align: right'>HTG %s</strong>" % (self.prix_double_nounou)
        return "%s %s" % (prix_client, prix_nounou)
    prix_pour_2_enfants.allow_tags = True

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.nom)


class Option(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Type Option")
    description = models.TextField(max_length=200, blank=True, verbose_name="Description")
    cout_client = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cout Client (USD)")
    cout_nounou = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cout Nounou (HTG)")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    actif = models.BooleanField(verbose_name="Actif")

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.nom)




