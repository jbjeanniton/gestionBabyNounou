from django.db import models
from base.models import Poste, Option, TypePrestation
from django.core.exceptions import ValidationError
from gestionBabyNounou.regex import regex_noid, regex_tel
from base.models import Zone
from math import floor
from datetime import date


def validate_salaire(value):
    if value > 5:
        raise ValidationError('%s ne correspond pas au bareme de ce poste!' % value)


# Create your models here.

class RessourceHumaine(models.Model):
    DEBUTANT = 1
    ELEMENTAIRE = 2
    INTERMEDIAIRE = 3
    AVANCE = 4

    NIVEAU_LANGUE = (
        (DEBUTANT, 'Debutant'),
        (ELEMENTAIRE, 'Elementaire'),
        (INTERMEDIAIRE, 'Intermediaire'),
        (AVANCE, 'Avance'),
    )

    CELIBATAIRE = "celibataire"
    MARIE = "marie"
    VEUF = "veuf"
    DIVORCE = "divorce"

    ETAT_MATRIMONIAL_LST = (
        (CELIBATAIRE, 'Celibataire'),
        (MARIE, 'Marie(e)'),
        (VEUF, 'Veuf/Veuve'),
        (DIVORCE, 'Divorce(e)'),
    )

    BAC_1 = "bac1"
    BAC_2 = "bac2"
    UNIVERSITAIRE = "universitaire"

    NIVEAU_ACADEMIQUE = (
        (BAC_1, 'BAC I'),
        (BAC_2, 'BAC II'),
        (UNIVERSITAIRE, 'Universitaire'),
    )

    F = "F"
    M = "M"

    SEXE = (
        (F, 'F'),
        (M, 'M'),
    )

    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    deuxieme_prenom = models.CharField(max_length=100, blank=True, verbose_name="Deuxième prénom")
    sexe = models.CharField(max_length=1, choices=SEXE, default="F")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    lieu_naissance = models.CharField(max_length=100, verbose_name="Lieu de naissance")
    no_id = models.CharField(max_length=20, verbose_name="ID/CIN", unique=True, validators=[regex_noid])
    nom_mere = models.CharField(max_length=100, blank=True, verbose_name="Nom de la mere")
    etat_matrimonial = models.CharField(max_length=20, choices=ETAT_MATRIMONIAL_LST, verbose_name="Etat matrimonial")
    religion = models.CharField(max_length=100, blank=True, verbose_name="Religion")
    nbr_enfant_charge = models.PositiveSmallIntegerField(default=0, verbose_name="Nbr enfant a charge")
    adresse = models.TextField(max_length=300, verbose_name="Adresse")
    zone = models.ForeignKey(Zone, null=True, blank=True)
    ville = models.CharField(max_length=100, verbose_name="Ville")
    tel_principal = models.CharField(max_length=20, verbose_name="No Telephone Principal", validators=[regex_tel])
    tel_secondaire = models.CharField(max_length=20, verbose_name="No Telephone Secondaire", validators=[regex_tel], blank=True)
    email = models.EmailField(verbose_name="Email")
    niveau = models.CharField(max_length=20, verbose_name="Niveau d'etude", choices=NIVEAU_ACADEMIQUE)
    formation = models.TextField(max_length=100, blank=True, verbose_name="Formation")
    niveau_francais = models.PositiveSmallIntegerField(blank=True, null=True, choices=NIVEAU_LANGUE,
                                                       verbose_name="Niveau francais")
    niveau_anglais = models.PositiveSmallIntegerField(blank=True, null=True, choices=NIVEAU_LANGUE, verbose_name="Niveau anglais")
    niveau_espagnol = models.PositiveSmallIntegerField(blank=True, null=True, choices=NIVEAU_LANGUE, verbose_name="Niveau Espagnol")
    no_compte = models.CharField(max_length=50, blank=True)
    nom_compte = models.CharField(max_length=100, blank=True)
    nom_banque = models.CharField(max_length=50, blank=True)
    note = models.TextField(max_length=200, blank=True, verbose_name="Note")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nom.upper() + " " + self.prenom


class Employe(models.Model):
    ressourcehumaine = models.OneToOneField(RessourceHumaine, verbose_name="Personne Ressource")
    poste = models.ForeignKey(Poste)
    date_debut = models.DateField(verbose_name="Date de debut")
    date_fin = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    salaire = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salaire Brut")
    note = models.TextField(max_length=200, blank=True, verbose_name="Note")
    actif = models.BooleanField(verbose_name="Actif")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.ressourcehumaine.nom.upper() + " " + self.ressourcehumaine.prenom


class Nounou(models.Model):
    ressourcehumaine = models.OneToOneField(RessourceHumaine, verbose_name="Personne Ressource")
    date_debut = models.DateField(verbose_name="Date de debut")
    date_fin = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    star = models.PositiveSmallIntegerField(default=3, verbose_name="Niveau")
    est_mere = models.BooleanField(verbose_name="Est une mère")
    note = models.TextField(max_length=200, blank=True, verbose_name="Note")
    actif = models.BooleanField(verbose_name="Actif")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    @property
    def anciennete(self):
        delta_date = date.today() - self.date_debut

        experimente_str = ''
        experimente = delta_date.days
        if experimente >= 365:
            experimente_str = "%s an(s)" % floor(experimente/365)
        elif experimente >=30:
            experimente_str = "%s moi(s)" % floor(experimente/30)
        elif experimente >=7:
            experimente_str = "%s semaine(s)" % floor(experimente/7)
        elif experimente > 0:
            experimente_str ="%s jour(s)" % experimente
        return experimente_str

    @property
    def experience(self):
        from gestionclient.models import Contrat
        delta_date = date.today() - self.date_debut
        experimente = 0

        for contrat in Contrat.objects.filter(nounou=self):
            date_d = contrat.date_debut if contrat.date_debut else date.today()
            date_f = contrat.date_fin_reel if contrat.date_fin_reel else date.today()
            delta_date = date_f - date_d
            experimente += delta_date.days

        experimente_str = ''
        #experimente = delta_date.days
        if experimente >= 365:
            experimente_str = "%s an(s)" % floor(experimente/365)
        elif experimente >=30:
            experimente_str = "%s moi(s)" % floor(experimente/30)
        elif experimente >=7:
            experimente_str = "%s semaine(s)" % floor(experimente/7)
        elif experimente > 0:
            experimente_str ="%s jour(s)" % experimente
        elif experimente == 0:
            experimente_str ="Aucune"
        return experimente_str

    def __str__(self):  # __unicode__ on Python 2
        return "%s %s" % (self.ressourcehumaine.prenom, self.ressourcehumaine.nom)


class Disponibilite(models.Model):
    nounou = models.ForeignKey(Nounou)
    typeprestation = models.ForeignKey(TypePrestation)
    libre = models.BooleanField(verbose_name="Libre")

    def __str__(self):  # __unicode__ on Python 2
        return self.typeprestation


class NounouOption(models.Model):
    nounou = models.ForeignKey(Nounou)
    option = models.ForeignKey(Option)

    def __str__(self):  # __unicode__ on Python 2
        return self.option
