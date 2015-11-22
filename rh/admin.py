from django.contrib import admin
from rh.models import RessourceHumaine, Employe, Nounou, Disponibilite, NounouOption


# Register your models here.

class DisponibiliteInline(admin.StackedInline):
    model = Disponibilite
    extra = 1

class NounouOptionInline(admin.StackedInline):
    model = NounouOption
    extra = 1


class RessourceHumaineAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info de base', {
            'fields': ['nom', 'prenom', 'deuxieme_prenom', 'date_naissance', 'lieu_naissance', 'no_id', 'nom_mere',
                       'etat_matrimonial', 'religion', 'nbr_enfant_charge']}),
        ('Coordonnées', {'fields': ['adresse', 'ville', 'tel_principal', 'tel_secondaire', 'email']}),
        ('Profil Academique', {'fields': ['niveau', 'formation', 'niveau_francais', 'niveau_anglais']}),
        ('Informations Bancaires', {'fields': ['no_compte', 'nom_compte', 'nom_banque']}),
        (None, {'fields': ['note']}),
    ]
    list_display = ("nom", "prenom", "no_id", "tel_principal", "niveau")


class EmployeAdmin(admin.ModelAdmin):
    list_display = ("ressourcehumaine", "poste", "date_debut", "salaire", "actif")


class OptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nom', 'description']}),
        ('Cout', {'fields': ['cout_client', 'cout_nounou']}),
        (None, {'fields': ['actif']}),
    ]
    list_display = ("nom", "cout_client", "cout_nounou", "actif")


class NounouAdmin(admin.ModelAdmin):
    list_display = ("ressourcehumaine", "date_debut", "anciennete", "experience", "star", "est_mere", "actif")
    search_fields = ["ressourcehumaine__nom", "ressourcehumaine__prenom"]
    list_filter = ('star','est_mere','actif')
    inlines = [DisponibiliteInline, NounouOptionInline]


# Added all in the register
admin.site.register(RessourceHumaine, RessourceHumaineAdmin)
admin.site.register(Employe, EmployeAdmin)
admin.site.register(Nounou, NounouAdmin)
#admin.site.register(Disponibilite)
#admin.site.register(NounouOption)
