from django.shortcuts import render
from django.http import JsonResponse
from facture.models import Facture, DetailsFacture, DetailsFactureOption, gen_facture
from decimal import Decimal
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, "public/index.html", {'menu_active':'accueil'})

def facture_view(request, code):
    facture = Facture.objects.get(code=code)
    details_facure = DetailsFacture.objects.filter(facture=facture)
    sub_total_show = True if len(details_facure) > 1 else False

    return render(request, "public/facture_view.html", {'menu_active':'accueil',
                                                        'mois': facture.moisfacture.mois,
                                                        'facture': facture, 'details': details_facure,
                                                        'sub_total_show': sub_total_show,
                                                        'sous_montant_total': facture.sous_montant_total,
                                                        'montant_total': facture.montant_total })

def facture_management(request):
    facture = Facture.objects.filter(moisfacture__mois="2015-12")
    return render(request, "public/facture_management.html", {'menu_active':'accueil',
                                                       'facture': facture, })

def facture_generate(request):
    result = gen_facture(request)
    return JsonResponse({'result': result})
