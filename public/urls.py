__author__ = 'jbjeanniton'
from django.conf.urls import include, url, patterns

urlpatterns = patterns('public.views',
    url(r'^$', 'home'),
    url(r'^facture/view/(?P<code>BN-[0-9]{4}[0-9]{4})/$', 'facture_view'),
    url(r'^facture/management/$', 'facture_management'),
    url(r'^facture/generate/$', 'facture_generate'),
)
