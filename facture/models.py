from django.db import models
from gestionclient.models import Client, Contrat, ContratOption
from base.models import Option, TypePrestation
from rh.models import Nounou
from gestionBabyNounou.common_lst import *
import uuid
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal, ROUND_UP, getcontext
from django.contrib.auth.models import Permission, User


# Create your models here.
class MoisFacture(models.Model):
    mois = models.CharField(max_length=7)
    genere = models.BooleanField(default=False)
    envoye = models.BooleanField(default=False)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    @property
    def mois_a_lire(self):
        return "%s" % timezone.datetime.strptime(self.mois+'-01', "%Y-%m-%d").strftime("%B %Y")

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % timezone.datetime.strptime(self.mois+'-01', "%Y-%m-%d").strftime("%B %Y")

class Facture(models.Model):
    client = models.ForeignKey(Client)
    moisfacture = models.ForeignKey(MoisFacture, verbose_name="mois")
    code = models.CharField(max_length=11, unique=True)
    token = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date = models.DateField()
    a_envoyer = models.BooleanField(default=True, verbose_name="Envoi par mail")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (("can_generate_facture", "Générer Factures"), ("can_send_facture", "Envoyer Factures"))

    @property
    def sous_montant_total(self):
        sous_montant_total = 0;
        for details in DetailsFacture.objects.filter(facture=self):
            sous_montant_total += details.montant_total

        return sous_montant_total

    @property
    def montant_total(self):
        montant_total_facture = self.sous_montant_total + self.balance
        return montant_total_facture

    def __str__(self):  # __unicode__ on Python 2
        return "Facture du %s pour %s" % (self.moisfacture, self.client)

class DetailsFacture(models.Model):
    facture = models.ForeignKey(Facture)
    typeprestation = models.ForeignKey(TypePrestation, blank=True, null=True)
    nounou = models.ForeignKey(Nounou, blank=True, null=True)
    personalise = models.BooleanField(default=False)
    nbr_enfant = models.PositiveSmallIntegerField(default=1, verbose_name="Nbr enfant")
    nbr_jour_mensuel = models.PositiveSmallIntegerField(default=26, verbose_name="Nbr de jour / mois")
    montant_prestation = models.DecimalField(max_digits=8, decimal_places=2)
    jour_absence = models.PositiveSmallIntegerField(default=0)
    heure_supplementaire = models.PositiveSmallIntegerField(default=0)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    @property
    def jour_travail(self):
        return self.nbr_jour_mensuel - self.jour_absence

    @property
    def montant_calcule(self):
        montant = Decimal(self.montant_prestation * self.jour_travail/self.nbr_jour_mensuel)
        return round(montant,2)

    @property
    def montant_heure_supp(self):
        montant = Decimal(self.heure_supplementaire * 2)
        return round(montant,2)

    @property
    def montant_total(self):
        montant = self.montant_calcule
        for option in DetailsFactureOption.objects.filter(detailsfacture=self):
            montant+= option.cout_option
        montant+=self.heure_supplementaire*2
        return round(montant,2)

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % self.typeprestation

class DetailsFactureOption(models.Model):
    detailsfacture = models.ForeignKey(DetailsFacture)
    option = models.ForeignKey(Option)
    cout_option = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cout Client (USD)")
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.option

class Versement(models.Model):
    client = models.ForeignKey(Client)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    devise = models.CharField(max_length=3, choices=DEVISE,)
    taux_du_jour = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    type = models.CharField(max_length=30, choices=TYPE_VERSEMENT)
    no_transaction = models.CharField(max_length=32, blank=True)
    date = models.DateField()
    note = models.TextField(max_length=200, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    utilise = models.BooleanField(default=False)

    @property
    def equivalent(self):
        return self.montant * self.taux

    def __str__(self):  # __unicode__ on Python 2
        return self.mois

class Payement(models.Model):
    facture = models.ForeignKey(Facture)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    devise = models.CharField(max_length=3, choices=DEVISE,)
    taux_du_jour = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    type = models.CharField(max_length=30, choices=TYPE_VERSEMENT)
    no_transaction = models.CharField(max_length=32, blank=True)
    date = models.DateField()
    note = models.TextField(max_length=200, blank=True)
    timestamp_add = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.mois


def last_code_int():
    today = datetime.now()
    mois = "%s-%s" % (today.year, today.month)
    facture = Facture.objects.filter(moisfacture__mois=mois).order_by('-pk').first()
    last_code = int(facture.code[8:]) if facture else 200
    return last_code

def gen_code(last_code_int):
    today = datetime.now()
    code = "BN-%s%s" % (today.year, str(last_code_int).zfill(4))
    return code


def gen_token():
    return uuid.uuid4()


def gen_facture(request):
    user = request.user
    if user.is_authenticated() & user.has_perm( 'facture.can_generate_facture' ):

        last_code = last_code_int()
        mois_facture = MoisFacture.objects.filter(genere=False, envoye=False).order_by('-mois').first()
        if mois_facture:
            for client in Client.objects.filter(actif=True):
                last_code+=1
                facture = Facture(client=client, moisfacture=mois_facture, code=gen_code(last_code), token=gen_token(),
                                  date=datetime.now().date())
                facture.save()
                for contrat in Contrat.objects.filter(client=client, actif=True, date_fin_reel__isnull=True):
                    details = DetailsFacture(facture=facture, typeprestation=contrat.typeprestation, nounou=contrat.nounou,
                                             personalise=contrat.personalise, nbr_enfant=contrat.nbr_enfant,
                                             nbr_jour_mensuel=contrat.nbr_jour_mensuel,
                                             montant_prestation=contrat.montant_prestation, jour_absence=0,
                                             heure_supplementaire=0)
                    details.save()
                    for contrat_option in ContratOption.objects.filter(contrat=contrat):
                        DetailsFactureOption(detailsfacture=details, option=contrat_option.option, cout_option=contrat_option.option.cout_client).save()

            mois_facture.genere=True
            mois_facture.save()
            return True
        else:
            return False
    else:
        return False
