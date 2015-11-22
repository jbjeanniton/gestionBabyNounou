__author__ = 'jbjeanniton'

DEPARTEMENT = "departement"
COMMUNE = "commune"
SECTION_COMMUNALE = "section_communale"

NIVEAU_ZONE = (
    (DEPARTEMENT, 'Département'),
    (COMMUNE, 'Commune'),
    (SECTION_COMMUNALE, 'Section Communale'),
)


F = "F"
M = "M"

SEXE = (
    (F, 'F'),
    (M, 'M'),
)

USD = "USD"
HTG = "HTG"

DEVISE = (
    (USD, 'USD'),
    (HTG, 'HTG'),
)

CASH = "Cash"
CHEQUE = "Chèque"
VIREMENT = "Virement bancaire"
CARTE_CREDIT = "Carte de crédit"

TYPE_VERSEMENT = (
    (CASH, 'Cash'),
    (CHEQUE, 'Cheque'),
    (VIREMENT, 'Virement'),
    (CARTE_CREDIT, 'Carte de credit'),
)
