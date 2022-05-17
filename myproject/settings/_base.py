"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import json
import sys
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ImproperlyConfigured
from myproject.apps.core.versioning import get_git_changeset_timestamp

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EXTERNAL_BASE = os.path.join(BASE_DIR, "externals")
EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "apps")
sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path


with open(os.path.join(os.path.dirname(__file__), 'secrets.json'), 'r') as f:
    secrets = json.loads(f.read())


def get_secret(setting):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} secret variable'
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
]


# Application definition

INSTALLED_APPS = [
    # contributed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.forms',
    # third-party
    'imagekit',
    'crispy_forms',
    'django_json_ld',
    'qr_code',
    'haystack',
    # ...
    # local
    'myproject.apps.core',
    'myproject.apps.ideas',
    'myproject.apps.categories',
    'myproject.apps.search',
    'myproject.apps.locations',
    # ...
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myproject', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'myproject.apps.core.context_processors.website_url',
                'myproject.apps.core.context_processors.google_maps',
            ],
            'libraries':{
                'custom_templatetag': 'myproject.apps.core.templatetags.utility_tags',
            }
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }}

GDAL_LIBRARY_PATH = '/opt/local/lib/libgdal.dylib'
GEOS_LIBRARY_PATH = '/opt/local/lib/libgeos_c.dylib'

# Password validation
# https://docs.djangoproject.com/en/3.1/topics/auth/passwords/#password-validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# All official languages of European Union
LANGUAGES = [
    ("bg", "Bulgarian"),    ("hr", "Croatian"),
    ("cs", "Czech"),        ("da", "Danish"),
    ("nl", "Dutch"),        ("en", "English"),
    ("et", "Estonian"),     ("fi", "Finnish"),
    ("fr", "French"),       ("de", "German"),
    ("el", "Greek"),        ("hu", "Hungarian"),
    ("ga", "Irish"),        ("it", "Italian"),
    ("lv", "Latvian"),      ("lt", "Lithuanian"),
    ("mt", "Maltese"),      ("pl", "Polish"),
    ("pt", "Portuguese"),   ("ro", "Romanian"),
    ("sk", "Slovak"),       ("sl", "Slovene"),
    ("es", "Spanish"),      ("sv", "Swedish"),
]

COUNTRY_CHOICES = [
    ("BE", _("Belgium")),
    ("BG", _("Bulgaria")),
    ("CZ", _("Czechia")),
    ("DK", _("Denmark")),
    ("DE", _("Germany")),
    ("EE", _("Estonia")),
    ("IE", _("Ireland")),
    ("EL", _("Greece")),
    ("ES", _("Spain")),
    ("FR", _("France")),
    ("HR", _("Croatia")),
    ("IT", _("Italy")),
    ("CY", _("Cyprus")),
    ("LV", _("Latvia")),
    ("LT", _("Lithuania")),
    ("LU", _("Luxembourg")),
    ("HU", _("Hungary")),
    ("MT", _("Malta")),
    ("NL", _("Netherlands")),
    ("AT", _("Austria")),
    ("PL", _("Poland")),
    ("PT", _("Portugal")),
    ("RO", _("Romania")),
    ("SI", _("Slovenia")),
    ("SK", _("Slovakia")),
    ("FI", _("Finland")),
    ("SE", _("Sweden")),
    ("UK", _("United Kingdom")),
]

LANGUAGES_EXCEPT_THE_DEFAULT = [
    (lang_code, lang_name)
    for lang_code, lang_name in LANGUAGES
    if lang_code != LANGUAGE_CODE
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject', 'site_static'),
]

timestamp = get_git_changeset_timestamp(BASE_DIR)
STATIC_URL = f'/static/{timestamp}/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MAGAZINE_ARTICLE_THEME_CHOICES = [
    ('futurism', _("Futurism")),
    ('nostalgia', _("Nostalgia")),
    ('sustainability', _("Sustainability")),
    ('wonder', _("Wonder")),
    ('positivity', _("Positivity")),
    ('solutions', _("Solutions")),
    ('science', _("Science")),
]

EMAIL_HOST = get_secret("EMAIL_HOST")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2

HAYSTACK_CONNECTIONS = {}
for lang_code, lang_name in LANGUAGES:
    lang_code_underscored = lang_code.replace("-", "_")
    HAYSTACK_CONNECTIONS[f"default_{lang_code_underscored}"] = {
        "ENGINE": "myproject.apps.search.multilingual_whoosh_backend.MultilingualWhooshEngine",
        "PATH": os.path.join(BASE_DIR, "tmp", f"whoosh_index_{lang_code_underscored}"),
    }
lang_code_underscored = LANGUAGE_CODE.replace("-", "_")
HAYSTACK_CONNECTIONS["default"] = HAYSTACK_CONNECTIONS[
    f"default_{lang_code_underscored}"
]

GOOGLE_MAPS_API_KEY = get_secret("GOOGLE_MAPS_API_KEY")
