"""
Django settings for gestionBabyNounou project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c(d@x085__)&q6f6d*(a6e%gpxf0b*!su9w-=@+zv0f3s)dz-='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'rh',
    'gestionclient',
    'facture',
    'public',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gestionBabyNounou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestionBabyNounou.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)


SUIT_CONFIG = {
    'ADMIN_NAME': 'Gestion Baby Nounou',
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU': (
         'sites',
         {'app': 'base', 'label': 'Structure de base', 'icon': 'icon-th-list'},
         {'app': 'rh', 'label': 'Ressources humaines', 'icon': 'icon-user', 'models': ('ressourcehumaine', 'employe', 'nounou')},
         {'app': 'gestionclient', 'label': 'Gestion Clients', 'icon': 'icon-briefcase', 'models': ('prospect', 'client', 'contrat')},
         {'app': 'facture', 'label': 'Factures et Payements', 'icon': 'icon-folder-close', 'models': ['Facture', {'label': 'Generer et Envoyer', 'url': '/facture/management/'}, 'MoisFacture', 'Payement', 'Versement']},
         {'app': 'rh', 'label': 'Payroll', 'icon': 'icon-gift'},
         {'app': 'auth', 'label': 'Gestion des droits', 'icon': 'icon-lock', 'models': ('user', 'group')},

     ),

}
