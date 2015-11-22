from django.contrib import admin
from gestionclient.models import Client, Enfant, Contrat, ContratOption, Prospect
from base.models import Option
from django.db.models import Sum


def activate(modeladmin, request, queryset):
    queryset.update(actif=True)
activate.short_description = "Activer les clients selectionnés"


def desactivate(modeladmin, request, queryset):
    queryset.update(actif=False)
desactivate.short_description = "Désactiver les clients selectionnés"

def to_client(modeladmin, request, queryset):
    for prospect in queryset:
        client = Client()
        client.nom = prospect.nom
        client.prenom = prospect.prenom
        client.deuxieme_prenom = prospect.deuxieme_prenom
        client.sexe = prospect.sexe
        client.adresse = prospect.adresse
        client.zone = prospect.zone
        client.tel_principal = prospect.tel_principal
        client.tel_secondaire = prospect.tel_secondaire
        client.email_principal = prospect.email_principal
        client.email_secondaire = prospect.email_secondaire
        client.note = prospect.note
        client.save()
        prospect.delete()
to_client.short_description = "Transformer les prospects selectionnés en clients"


class EnfantInline(admin.StackedInline):
    model = Enfant
    extra = 1

class ContratOptionInline(admin.StackedInline):
    model = ContratOption
    extra = 1
    verbose_name = 'Options'


class ProspectAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "tel", "email", "adresse", "zone")
    search_fields = ["nom", "prenom", "tel_principal", "tel_secondaire", "email_principal", "email_secondaire"]
    list_filter = ('zone',)
    ordering = ["nom"]
    actions = [to_client]

class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "tel", "email", "adresse", "zone", "actif")
    inlines = [EnfantInline]
    search_fields = ["nom", "prenom", "tel_principal", "tel_secondaire", "email_principal", "email_secondaire"]
    list_filter = ('actif', 'zone',)
    ordering = ["nom"]
    actions = [activate, desactivate]


class ContratAdmin(admin.ModelAdmin):
    list_display = ("client", "typeprestation", "personalise", "nbr_enfant", "nbr_jour_mensuel", "montant_prestation", "montant_total", "date_debut", "date_fin_prevue", "actif")
    search_fields = ["client__nom", "client__prenom"]
    list_filter = ('actif', 'typeprestation',)
    ordering = ["client"]
    actions = [activate, desactivate]
    inlines = [ContratOptionInline]




# Register your models here.

admin.site.register(Client, ClientAdmin)
admin.site.register(Contrat, ContratAdmin)
admin.site.register(Prospect, ProspectAdmin)
# admin.site.register(ClientEnfant)
