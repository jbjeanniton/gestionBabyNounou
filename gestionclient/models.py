from django.db import models
from gestionBabyNounou.regex import regex_noid, regex_tel
from gestionBabyNounou.common_lst  import *
from rh.models import Nounou
from base.models import Zone, TypePrestation, Option



# Create your models here.

class Prospect(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    deuxieme_prenom = models.CharField(max_length=100, blank=True, verbose_name="Deuxième prénom")
    sexe = models.CharField(max_length=1, choices=SEXE, default="F")
    adresse = models.TextField(max_length=300, null=True, blank=True)
    zone = models.ForeignKey(Zone, null=True, blank=True)
    tel_principal = models.CharField(max_length=20, verbose_name="No Telephone Principal", validators=[regex_tel],
                                     blank=True)
    tel_secondaire = models.CharField(max_length=20, verbose_name="No Telephone Secondaire", validators=[regex_tel],
                                      blank=True)
    email_principal = models.EmailField(verbose_name="Email Principal", blank=True)
    email_secondaire = models.EmailField(verbose_name="Email Secondaire", blank=True)
    note = models.TextField(max_length=200, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def tel(self):
        return "%s <br> %s " % (self.tel_principal, self.tel_secondaire)
    tel.allow_tags = True

    def email(self):
        email_principal = '' if self.email_principal == '' else '<a href="mailto:%s"> %s </a>' % (self.email_principal, self.email_principal)
        email_secondaire = '' if self.email_secondaire == '' else '<br><a href="mailto:%s"> %s </a>' % (self.email_secondaire, self.email_secondaire)
        return "%s %s " % (email_principal, email_secondaire)
    email.allow_tags = True

    def __str__(self):  # __unicode__ on Python 2
        return self.nom.upper() + " " + self.prenom

class Client(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    deuxieme_prenom = models.CharField(max_length=100, blank=True, verbose_name="Deuxième prénom")
    sexe = models.CharField(max_length=1, choices=SEXE, default="F")
    no_id = models.CharField(max_length=20, verbose_name="ID/CIN", validators=[regex_noid], blank=True, null=True)
    adresse = models.TextField(max_length=300, null=True, blank=True)
    zone = models.ForeignKey(Zone, null=True, blank=True)
    tel_principal = models.CharField(max_length=20, verbose_name="No Telephone Principal", validators=[regex_tel],
                                     blank=True)
    tel_secondaire = models.CharField(max_length=20, verbose_name="No Telephone Secondaire", validators=[regex_tel],
                                      blank=True)
    email_principal = models.EmailField(verbose_name="Email Principal", blank=True)
    email_secondaire = models.EmailField(verbose_name="Email Secondaire", blank=True)
    note = models.TextField(max_length=200, blank=True)
    actif = models.BooleanField(default=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (("can_activate_client", "Activer Client"),)

    def tel(self):
        return "%s <br> %s " % (self.tel_principal, self.tel_secondaire)
    tel.allow_tags = True

    def email(self):
        email_principal = '' if self.email_principal == '' else '<a href="mailto:%s"> %s </a>' % (self.email_principal, self.email_principal)
        email_secondaire = '' if self.email_secondaire == '' else '<br><a href="mailto:%s"> %s </a>' % (self.email_secondaire, self.email_secondaire)
        return "%s %s " % (email_principal, email_secondaire)
    email.allow_tags = True

    def __str__(self):  # __unicode__ on Python 2
        return self.nom.upper() + " " + self.prenom


class Enfant(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True)
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    deuxieme_prenom = models.CharField(max_length=100, blank=True, verbose_name="Deuxième prénom")
    sexe = models.CharField(max_length=1, choices=SEXE, default="F")
    date_naissance = models.DateField(verbose_name="Date de naissance", blank=True, null=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom.upper() + " " + self.prenom


class Contrat(models.Model):
    client = models.ForeignKey(Client, limit_choices_to={'actif': True})
    typeprestation = models.ForeignKey(TypePrestation)
    nounou = models.ForeignKey(Nounou, blank=True, null=True)
    personalise = models.BooleanField(default=False)
    nbr_enfant = models.PositiveSmallIntegerField(default=1, verbose_name="Nbr enfant")
    nbr_jour_mensuel = models.PositiveSmallIntegerField(default=26, verbose_name="Nbr de jour / mois")
    montant_prestation = models.DecimalField(max_digits=8, decimal_places=2)
    date_debut = models.DateField(verbose_name="Date de Début", blank=True, null=True)
    date_fin_prevue = models.DateField(verbose_name="Date de Fin", blank=True, null=True)
    date_fin_reel = models.DateField(verbose_name="Date de Fin Réel", blank=True, null=True)
    actif = models.BooleanField(default=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    @property
    def fin_contrat(self):
        if self.date_fin_reel__isnul:
            return False
        else:
            return True

    @property
    def montant_total(self):
        montant = self.montant_prestation
        for option in ContratOption.objects.filter(contrat=self):
            montant+= option.option.cout_client
        return montant

    def __str__(self):  # __unicode__ on Python 2
        return "%s | Plan : %s" % (self.client, self.typeprestation)

class ContratOption(models.Model):
    contrat = models.ForeignKey(Contrat)
    option = models.ForeignKey(Option)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.option.nom