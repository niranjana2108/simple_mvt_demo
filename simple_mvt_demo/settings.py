from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'test-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'students',
]

MIDDLEWARE = []

ROOT_URLCONF = 'simple_mvt_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

WSGI_APPLICATION = 'simple_mvt_demo.wsgi.application'
