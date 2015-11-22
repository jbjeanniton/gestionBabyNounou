from django.contrib import admin
from facture.models import MoisFacture, Facture, DetailsFacture, DetailsFactureOption, Versement, Payement

class DetailsFactureInline(admin.StackedInline):
    model = DetailsFacture
    extra = 1


class FactureAdmin(admin.ModelAdmin):
    list_display = ("code", "client", "moisfacture", "sous_montant_total", "balance", "montant_total","a_envoyer","date")
    search_fields = ["code", "client__nom", "client__prenom"]
    list_filter = ('moisfacture__mois',)
    ordering = ["-moisfacture__mois", "code"]
    # actions = [activate, desactivate]
    inlines = [DetailsFactureInline]

# Register your models here.
admin.site.register(MoisFacture)
admin.site.register(Facture, FactureAdmin)
admin.site.register(DetailsFacture)
admin.site.register(DetailsFactureOption)
admin.site.register(Versement)
admin.site.register(Payement)