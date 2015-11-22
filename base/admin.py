from django.contrib import admin
from base.models import Poste, TypePrestation, Option, Zone

# Register your models here.


class PosteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nom', 'description']}),
        ('Barème salarial', {'fields': ['salaire_min', 'salaire_max']}),
    ]
    list_display = ("nom", "salaire_min", "salaire_max")


class TypePrestationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nom', 'horaire']}),
        ('Prix de base', {'fields': ['prix_base_client', 'prix_base_nounou']}),
        ('Prix pour 2 enfants', {'fields': ['prix_double_client', 'prix_double_nounou']}),
        (None, {'fields': ['actif']}),
    ]
    list_display = ("nom", "horaire", "prix_de_base", "prix_pour_2_enfants", "actif")
    ordering = ["id"]


class OptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nom', 'description']}),
        ('Cout', {'fields': ['cout_client', 'cout_nounou']}),
        (None, {'fields': ['actif']}),
    ]
    list_display = ("nom", "cout_client", "cout_nounou", "actif")

class ZoneAdmin(admin.ModelAdmin):
    list_display = ("nom", "type")


# Added all in the register
admin.site.register(Poste, PosteAdmin)
admin.site.register(TypePrestation, TypePrestationAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Zone, ZoneAdmin)
